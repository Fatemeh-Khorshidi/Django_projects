from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView

from todo.forms import TasksForm
from todo.models import Task, Category


class TasksListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'all_tasks'


class TasksDetailsView(DetailView):
    model = Task
    template_name = 'task_Details_view.html'


# فانکشن نمیدونم چی چی
# class Taskss(request):
#     if request.method == 'POST':
#         forms = TasksForm(request.POST)
#
#         forms = Task(title=request.POST['title'], description=request.POST['description'],
#                     priority=request.POST['priority'])
#         forms.save()
#
#
#
#     tasks = Task.objects.all()
#     return render(request,'forms.html ', {forms:forms})


# def TasksViews(View):
#     pass
# def get(self.request, *args, **kwargs):
#     form =


class CategoryListView(ListView):
    model = Category
    template_name = 'Category_list.html'
    context_object_name = 'all_categories'
    queryset = Category.objects.get_null_category()


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'Category_detail.html'


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)
