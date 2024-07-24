from django.shortcuts import render, redirect
from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.
"""
Navigate to login page
"""
class SignInView(LoginView):
    template_name = 'to_do/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


"""
Navigate to registration page
"""
class RegisterView(generic.FormView):
    template_name = 'to_do/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterView, self).get(*args, **kwargs)


"""
Display task list
"""
class TaskList(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input
        return context


"""
Display task
"""
class TaskDetail(LoginRequiredMixin, generic.DetailView):
    model = Task
    context_object_name = 'task'


"""
Create a new task
"""
class TaskCreate(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


"""
Edit/Update task
"""
class TaskUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('index')


"""
Delete task
"""
class DeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
