from django import forms
from .models import User


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'photo']

    photo = forms.ImageField(required=False, widget=forms.FileInput)
    
    
class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
