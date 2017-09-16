from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .models import Todo
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    if request.method == 'POST':
        title = request.POST['title']
        todo = Todo(title=title)
        todo.save()
        return render(request,'index.html',context)
    else:
        return render(request,'index.html',context)

def show_completed(request):
    todos = Todo.objects.filter(completed=True)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def show_active(request):
    todos = Todo.objects.filter(completed=False)
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)
def clear_completed(request):
    Todo.objects.filter(completed=True).delete()
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'index.html', context)

def save_state(request):
    if request.method == 'POST':
        titles = dict(request.POST).keys()
        for title in Todo.objects.filter(title__in=titles):
            title.completed = True
            title.save()
        for title in Todo.objects.exclude(title__in=titles):
            title.completed = False
            title.save()
    
    return HttpResponseRedirect('/todos')
