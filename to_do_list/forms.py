from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
	deadline = forms.DateField(widget = forms.DateInput(attrs = {'type': 'date'}))
	description = forms.CharField(widget = forms.Textarea(attrs = {'style': 'height: 100px'}))
	
	class Meta:
		model = ToDo
		fields = ['title', 'description', 'deadline']
