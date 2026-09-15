from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == "POST":
        user_title = request.POST.get('title')
        user_desc = request.POST.get('description')
        Task.objects.create(title=user_title, description=user_desc)
        return redirect('task_list')
    return render(request, 'todo/create_task.html')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
