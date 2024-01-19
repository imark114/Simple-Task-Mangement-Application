from django.shortcuts import render, redirect
from .forms import AddTask
from .models import Task
# Create your views here.

def addTask(request):
    if request.method == 'POST':
        task_form = AddTask(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    task_form = AddTask()
    return render(request,'add_task.html',{'form': task_form})

def editTask(request, id):
    task = Task.objects.get(pk=id)
    task_form = AddTask(instance=task)
    if request.method == 'POST':
        task_form = AddTask(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    return render(request,'add_task.html',{'form': task_form})

def deleteTask(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')