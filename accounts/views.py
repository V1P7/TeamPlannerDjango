from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import SignUpForm, SignInForm


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			return redirect('signin')
	else:
		form = SignUpForm()
	
	return render(request, 'accounts/signup.html', {'form': form})


def signin(request):
	if request.method == 'POST':
		
		form = SignInForm(request.POST)
		
		if form.is_valid():
			
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			
			user = authenticate(request, username = username, password = password)
			
			if user is not None:
				login(request, user)
				return redirect('team_panel')
	
	else:
		form = SignInForm()
	
	return render(request, 'accounts/signin.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('signin')

