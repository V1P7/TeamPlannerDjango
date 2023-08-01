from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
	deadline = forms.DateField(widget = forms.DateInput(attrs = {'type': 'date'}))
	
	class Meta:
		model = ToDo
		fields = ['title', 'description', 'deadline']
