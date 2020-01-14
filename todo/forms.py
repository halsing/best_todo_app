from django import forms
from django.forms.models import inlineformset_factory

from .models import TodoList, Todo


class TodoForm(forms.Form):
    text = forms.CharField(max_length=100)
