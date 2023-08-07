from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from accounts.models import User
from main_dev.views import get_vacation_days


def index_projects(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            form.save_m2m()  # Save the many-to-many relationships (selected developers)
            return redirect('index_projects')
    else:
        form = ProjectForm()

    user, created = User.objects.get_or_create(username=request.user.username)
    projects = Project.objects.filter(user=request.user)
    developers = Project.objects.filter(developers=request.user)
    vacation_days = get_vacation_days(request)
    titleProjects = "open"
    context = {
        'titleProjects': titleProjects,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'position': user.position,
        'image': user.image,
        'projects': projects,
        'developers': developers,
        'form': form,
	    'vacation_days': vacation_days,
    }
    return render(request, 'projects/index.html', context)


def create_project(request):
	user, created = User.objects.get_or_create(username=request.user.username)
	titleCreateProject = "open"
	if request.method == 'POST':
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit = False)
			project.user = request.user
			project.save()
			return redirect('index_projects')
	else:
		form = ProjectForm()
	context = {
		'titleCreateProject': titleCreateProject,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form': form,
	}
	return render(request, 'projects/create_project.html', context)


def edit_project(request, pk):
	user, created = User.objects.get_or_create(username = request.user.username)
	project = Project.objects.get(pk = pk)
	if request.method == 'POST':
		form = ProjectForm(request.POST, instance = project)
		if form.is_valid():
			form.save()
			return redirect('index_projects')
	
	form = ProjectForm(instance = project)
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form': form,
	}
	return render(request, 'projects/edit_project.html', context)


def complete_project(request, pk):
	project = Project.objects.get(pk = pk)
	project.is_complete = True
	project.save()
	return redirect('index_projects')


def delete_project(request, pk):
	project = Project.objects.get(pk = pk)
	project.delete()
	return redirect('index_projects')