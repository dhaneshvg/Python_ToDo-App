from django.shortcuts import render
from .models import Task


# Create your views here.

def task_view(request):
    display = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        obj = Task(name=name, priority=priority)
        obj.save()
    return render(request, 'task_view.html', {'tasks': display})



