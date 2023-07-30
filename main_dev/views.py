from django.shortcuts import render
from accounts.models import User


def index(request):
	user, created = User.objects.get_or_create(username=request.user.username)
	title = "title"
	context = {
		'title': title,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
	}
	return render(request, 'main_dev/index.html', context)
