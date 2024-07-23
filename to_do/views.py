from django.shortcuts import render
from django.views import generic
from .models import Task
from django.urls import reverse_lazy


# Create your views here.
class TaskList(generic.ListView):
    model = Task
    context_object_name = 'tasks'
   

class TaskDetail(generic.DetailView):
    model = Task
    context_object_name = 'task'
    
class TaskCreate(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')

class TaskUpdate(generic.UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('index')

class DeleteView(generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')