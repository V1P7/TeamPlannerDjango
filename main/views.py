from django.shortcuts import render


def index(request):
	title = "Главная страница"
	
	context = {
		'title': title,
	}
	return render(request, 'main/index.html', context)