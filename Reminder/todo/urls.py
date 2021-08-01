from django.contrib import admin
from django.urls import path
from .views import TasksDetailsView, TasksListView

urlpatterns = [
    # path('',Taskss , name = 'tasks'),
    # path('admin/', admin.site.urls , name ='admin'),
    path('', TasksListView.as_view(), name='TaskList'),
    path('task/<int:pk>/', TasksDetailsView.as_view(),
         name='TaskDetail'),
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
]
