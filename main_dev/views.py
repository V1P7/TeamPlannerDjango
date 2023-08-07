from datetime import datetime

from django.shortcuts import render
from accounts.models import User


def index(request):
	user, created = User.objects.get_or_create(username=request.user.username)
	title = "title"
	current_date = datetime.now()
	join_date_datetime = datetime.combine(user.join_date, datetime.min.time())
	days = (current_date - join_date_datetime).days
	vacation_days = round((days / 365) * 28, 1)
	context = {
		'title': title,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'vacation_days': vacation_days
	}
	return render(request, 'main_dev/index.html', context)
