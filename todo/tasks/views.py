from django.shortcuts import render, get_object_or_404
from .models import Task
from django.http import HttpResponse
from .forms import TaskForm


def helloWorld(request):
    return HttpResponse("Hello World!")


def get_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def task_details(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(task)
    return render(request, 'tasks/task-details.html', {
        'task': task,
        'form': form
        })
