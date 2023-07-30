from django.shortcuts import render

from accounts.models import User


def to_do_list(request):
	user, created = User.objects.get_or_create(username = request.user.username)
	titleToDo = "open"
	context = {
		'titleToDo': titleToDo,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
	}
	return render(request, 'to_do_list/index.html', context)
