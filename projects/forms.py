from django import forms
from accounts.models import User
from .models import Project


class ProjectForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset = User.objects.all())
    developers = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Project
        fields = ['title_name', 'description', 'deadline', 'user', 'developers', 'status']
        
        widgets = {'deadline': forms.DateTimeInput(attrs = {'type': 'datetime-local'}), }