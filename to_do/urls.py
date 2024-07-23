from . import views
from django.urls import path


urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-details'),
    path('task-create/', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.DeleteView.as_view(), name='task-delete'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='login'), name='logout')
]