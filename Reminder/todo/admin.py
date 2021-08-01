from django.contrib import admin

# Register your models here.
from todo.models import Task,Category

admin.site.register(Task)
admin.site.register(Category)

