from django import forms

from .models import Task

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'description',
            'is_done'
        )