from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoforms


# Create your views here.

def task_view(request):
    display = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    return render(request, 'task_view.html', {'tasks': display})


def update(request, updateid):
    task = Task.objects.get(id=updateid)
    form = Todoforms(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': form})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})
