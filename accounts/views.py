
from django.shortcuts import redirect, render

from .forms import SignUpForm


def signup(request):
	form = SignUpForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			# процедура сохранения пароля
			return redirect('index')
	else:
		form = SignUpForm()
	
	return render(request, 'accounts/signup.html', {'form': form})