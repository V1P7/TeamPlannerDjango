from datetime import datetime
from django.shortcuts import render
from accounts.models import User


def get_vacation_days(request):
    user, created = User.objects.get_or_create(username=request.user.username)
    current_date = datetime.now()

    if user.join_date:
        join_date_datetime = datetime.combine(user.join_date, datetime.min.time())
        days = (current_date - join_date_datetime).days
        vacation_days = round((days / 365) * 28, 1)
        return vacation_days
    else:
        return 0


def index(request):
	user, created = User.objects.get_or_create(username = request.user.username)
	title = "title"
	vacation_days = get_vacation_days(request)
	context = {
		'title': title,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'vacation_days': vacation_days,
	}
	return render(request, 'main_dev/index.html', context)
