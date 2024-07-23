from django.shortcuts import render
from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView


# Create your views here.
class SignInView(LoginView):
    template_name = 'to_do/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

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