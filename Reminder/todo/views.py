from datetime import timezone

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView # new
from todo.forms import TasksForm
from todo.models import Task, Category


class TasksListView(ListView):
    # لیست تسک هاي تعریف شده
    model = Task
    # template_name = 'task_view.html'
    template_name = 'taskList.html'
    context_object_name = 'all_tasks'


class ExpiredTasks(ListView):
    model = Task
    template_name = 'task_expire_view.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expired_task']= Task.objects.expired_task()
        return context


class TasksDetailsView(DetailView):
    # جزییات هر تسک
    model = Task
    template_name = 'task_Details_view.html'

class TaskCreateView(CreateView):
    # برای ایجاد تسک جدید در صفحات html
    model = Task
    template_name = 'forms.html'
    fields = ['title', 'description', 'priority']



class CategoryListView(ListView):
    # لیست دسته بندي هاي موجود
    model = Category
    template_name = 'Category_list.html'
    context_object_name = 'all_categories'
    # queryset = Category.objects.get_null_category()
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['null_category']= Category.objects.get_null_category()
        context['full_category']= Category.objects.get_full_category()

        return context



class CategoryDetailView(ListView):
    # نمایش تسک هاي مربوط به هر دسته بندي
    model = Category
    template_name = 'Category_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        print(pk)
        # context['tasks'] = Task.objects.filter(category= pk)
        # context['tasks'] = Category.objects.get(pk = pk).task_set
        context['tasksss'] =  Task.objects.filter(category__id =pk)

        return context




# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ولی کار نمیکنه!!!!!!
def index(request):
    tasks = Task.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'taskList.html', context)


def updateTask(request, pk):
    # با استفاده از یک button دز صفحه اصلی هر تسک را آپدیت کنیم
    task = Task.objects.get(id=pk)

    form = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'update_task.html', context)


def deleteTask(request, pk):
    # با استفاده از یک button دز صفحه اصلی هر تسک را پاک کنیم

    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'delete.html', context)
