from django import forms
from .models import ToDo, BossTask


class ToDoForm(forms.ModelForm):
	deadline = forms.DateField(widget = forms.DateInput(attrs = {'type': 'date'}))
	description = forms.CharField(widget = forms.Textarea(attrs = {'style': 'height: 100px'}))
	
	class Meta:
		model = ToDo
		fields = ['title', 'description', 'deadline']


class BossTaskForm(forms.ModelForm):
	class Meta:
		model = BossTask
		fields = ['title', 'description', 'deadline', 'user', 'date']
		
		widgets = {'date': forms.DateTimeInput(attrs = {'type': 'datetime-local'}),
		           'deadline': forms.DateTimeInput(attrs = {'type': 'datetime-local'}),}

