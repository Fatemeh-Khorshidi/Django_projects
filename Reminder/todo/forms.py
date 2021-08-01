
from django import forms
from django.forms import ModelForm

from .models import *


class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
    PRIORITIES = [
        (0, 'بی اهمیت'),
        (1, 'کم اهمیت'),
        (2, 'توجه'),
        (3, 'قابل توجه'),
        (4, 'مهم'),
        (5, 'ضروری'),

    ]
    # title
    title = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Add new task...'}))
    # description
    description = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
    # priority
    priority = forms.ChoiceField(choices=PRIORITIES)





