from . import views
from django.urls import path


urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-details'),
]