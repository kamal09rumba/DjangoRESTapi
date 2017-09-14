from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from models import Todo
def index(request):
    todos = Todo.objects.all()[:10]
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
