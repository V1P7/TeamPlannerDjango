from urllib import request
from django.shortcuts import render


def signup(request):
	title = 'Sign Up'
	context = {
		'title': title
	}
	return render(request, 'accounts/signup.html', context)


def signin(request):
	title = 'Sign In'
	context = {
		'title': title
	}
	return render(request, 'accounts/signin.html', context)


# def logout_user(request):
#     logout(request)
#     return redirect('login')
