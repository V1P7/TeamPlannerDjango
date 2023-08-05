from django.shortcuts import render
from accounts.models import User


def index_projects(request):
	user, created = User.objects.get_or_create(username=request.user.username)
	titleProjects = "open"
	context = {
		'titleProjects': titleProjects,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
	}
	return render(request, 'projects/index.html', context)
