from django.shortcuts import render


def index(request):
	title = "Главная страница"
	context = {
		'title': title,
	}
	return render(request, 'main_dev/index.html', context)
