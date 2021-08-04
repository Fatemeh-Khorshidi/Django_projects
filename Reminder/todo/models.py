from datetime import datetime

from django.db import models
from django.urls import reverse
import datetime


class CategoryManager(models.Manager):
    def get_null_category(self):
        null_category = Category.objects.filter(
            task__isnull=True
        )
        return null_category

    def get_full_category(self):
        return Category.objects.filter(task__isnull=False)


class TaskManager(models.Manager):
    def expired_task(self):
        #     # تسک هایی که زمان آنها سر رسیده است
        expire_task = Task.objects.filter(EndDateTimeField__lte=datetime.date.today())
        return expire_task


# Create your models here.
class Task(models.Model):
    class Meta:
        ordering = ['EndDateTimeField']

    PORITY_TASK = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),

    ]
    # title
    title = models.CharField(max_length=40)
    # description
    description = models.TextField()
    # category
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    # priority
    priority = models.IntegerField(choices=PORITY_TASK)
    # ded line
    EndDateTimeField = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    # create at...
    created = models.DateTimeField(auto_now_add=True)
    # update at...
    updated = models.DateTimeField(auto_now=True)
    # filters all ended tasks
    objects = TaskManager()

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('task_Details_view', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=120)
    # filters categories
    objects = CategoryManager()

    def get_absolute_url(self):
        return reverse('Category_detail', args=[str(self.id)])
