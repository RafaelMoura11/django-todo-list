from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
from django.contrib import messages


def get_tasks(request):
    task_list = Task.objects.all().order_by('-created_at')
    paginator = Paginator(task_list, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)

    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def task_details(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task-details.html', {'task': task})


def edit_task(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edit-task.html', {
                'form': form, 'task': task})
    else:
        return render(request, 'tasks/edit-task.html', {
            'form': form, 'task': task})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/create-task.html', {'form': form})


def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    current_page_number = request.POST.get("current_page_number", " ")

    messages.info(request, 'Tarefa deletada com sucesso!')

    return redirect(f'/?page={current_page_number}/')


def change_status(request, id):
    task = get_object_or_404(Task, pk=id)
    task.done = not task.done

    task.save()

    return redirect('/')
