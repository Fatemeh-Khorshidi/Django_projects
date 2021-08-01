from datetime import datetime

from django.db import models

class CategoryManager(models.Manager):
    def get_null_category(self):
        null_category =Category.objects.filter(
            task__isnull=True
        )
class EndTimeManager(models.Manager):
    def get_queryset(self):
        # تسک هایی که زمان آنها سر رسیده است
        return super().get_queryset().filter(EndDateTimeField__lte=datetime.date.today())

class NoTaskManager(models.Manager):
    def get_queryset(self):
        pass
        # کتگوری هایی که هیچ تسکی در آن وجود ندارد
        # return category.objects.filter(tasks_ _isnull=True)
        # return Entry.objects.filter(category.tasks__isnull=True)


# Create your models here.
class Task(models.Model):
    class Meta :
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
    EndDateTimeField = models.DateTimeField(auto_now_add = False, auto_now = False,blank=True, null=True)
    # create at...
    created = models.DateTimeField(auto_now_add=True)
    # update at...
    updated = models.DateTimeField(auto_now=True)
    # filters all ended tasks
    EndedTasks = EndTimeManager()
    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=120)
    # filters categories
    categories =CategoryManager()