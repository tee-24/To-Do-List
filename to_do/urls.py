from . import views
from django.urls import path


urlpatterns = [
    path('', views.tasks, name='index'),
]