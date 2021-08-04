from django.contrib import admin
from django.urls import path
from .views import TasksDetailsView, TasksListView, deleteTask, updateTask, TaskCreateView, CategoryListView, \
    CategoryDetailView, ExpiredTasks

urlpatterns = [

    # tasks list
    path('', TasksListView.as_view(), name='TaskList'),
    # tasks view
    path('task/<int:pk>/', TasksDetailsView.as_view(), name='TaskDetail'),
    # update task
    path('update_task/<str:pk>/', updateTask, name="update_task"),
    # delete task
    path('delete/<str:pk>/', deleteTask, name="delete"),
    # create new task in navbar
    path('task/new/', TaskCreateView.as_view(), name='task_new'),
    #-------------------------------------------------------
    # categories list
    path('categories/', CategoryListView.as_view(), name='CategoryList'),
    # categories details
    path('<str:pk>/detail', CategoryDetailView.as_view(), name='CategoryDetail'),
    #expire tasks
    path('expired_tasks/', ExpiredTasks.as_view(), name='ex_list'),
]
