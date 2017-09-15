from django.shortcuts import render
# Create your views here.
from django.core.paginator import Paginator
from models import Todo
import pdb;
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
        title = request.POST.get('todo_title', '')
        checked = request.POST.get('checked', '')
        todo = Todo.objects.get(title=title)
        todo.completed = checked
        todo.save()
