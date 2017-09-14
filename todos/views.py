from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator
from models import Todo
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
    pass
