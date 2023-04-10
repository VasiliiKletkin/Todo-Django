from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    return render(request, 'todolist/index.html', context)


@require_http_methods(['POST'])
def add(request):
    title = request.POST.get('title')
    todo = Todo(title = title)
    todo.save()
    return redirect('index')

def update(request, todo_id = None):
    todo = Todo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')

def delete(request, todo_id = None):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')

