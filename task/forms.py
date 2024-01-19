from django import forms
from .models import Task

class AddTask(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            ' assigned_date': forms.DateInput(attrs={'class': 'datepicker'})
        }