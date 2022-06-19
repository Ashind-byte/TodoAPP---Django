from django import forms
from django.forms import ModelForm

from .models import TodoModel


class TodoForm(ModelForm):
    class Meta:
        model = TodoModel
        fields = '__all__'
        widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }