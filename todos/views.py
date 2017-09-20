from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Todo
from django.http import HttpResponse
from django.contrib import auth
from forms import UserForm


def index(request):
    print request.POST
    uname = request.session.get('uname')
    # uname2=request.user.username
    todos = Todo.objects.filter(author=uname)
    context = {
        'uname': uname,
        'todos': todos
    }
    if request.method == 'POST':
        print request.POST
        title = request.POST.get('title','')
        author = request.POST.get('author','')
        todo = Todo(title=title,author=author)
        todo.save()
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)

def show_completed(request):
    uname = request.session.get('uname')
    todos = Todo.objects.filter(completed=True,author=uname)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def show_active(request):
    uname = request.session.get('uname')
    todos = Todo.objects.filter(completed=False,author=uname)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)
def clear_completed(request):
    uname = request.session.get('uname')
    Todo.objects.filter(completed=True,author=uname).delete()
    return HttpResponseRedirect('/todos')

def save_state(request):
    print request.POST
    if request.method == 'POST':
        uname = request.session.get('uname')
        titles = dict(request.POST).keys()
        for title in Todo.objects.filter(title__in=titles):
            title.completed = True
            title.save()
        for title in Todo.objects.exclude(title__in=titles):
            title.completed = False
            title.save()
    return HttpResponseRedirect('/todos')

def search(request):
    language='uni-NEP'
    session_language='en-gb'
    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    return render(request,'search.html',{'language':language,'session_language':session_language})


def language(request,language='en-gb'):
    ##language setter
    response=HttpResponse("settign language to %s " % language)
    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response

def login(request):
    return render(request,'login.html')

def auth_view(request):
    username = request.POST.get('username','')  #pass the post value 'username' else if not present give empty string ''
    password = request.POST.get('password','')
    request.session['uname'] = username
    print request.POST
    print username
    print password
    user = auth.authenticate(username=username, password=password)  #returns user object if match else None
    if user is not None:
        auth.login(request, user)  #make user status as logged in now using django login function
        return HttpResponseRedirect('/todos')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render(request,'index.html',{'full_name': request.user.username})

def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/todos')

    #return render(request,'logout.html')

def signup(request):
    template_name = 'signup.html'
    registrationForm = UserForm(request.POST or None)
    context = {"registrationForm": registrationForm}
    if registrationForm.is_valid():
        user = registrationForm.save(commit=False)
        password = registrationForm.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        auth.login(request,user)
        return HttpResponseRedirect('/todos')
    return render(request, template_name, context)
