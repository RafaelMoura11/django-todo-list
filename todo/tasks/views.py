from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def helloWorld(request):
    return HttpResponse("Hello World!")


def get_tasks(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'tasks/tasks.html', {'tasks': tasks})
