from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Task


# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'

    def get(self, request, *args, **kwargs):
        display = Task.objects.all()
        return render(request, self.template_name, {'tasks': display})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('name')
            priority = request.POST.get('priority')
            date = request.POST.get('date')
            obj = Task(name=name, priority=priority, date=date)
            obj.save()
        return redirect('cbvtask')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name', 'priority', 'date']

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')
