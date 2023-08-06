from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
from accounts.models import User


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
    titleProjects = "open"
    context = {
        'titleProjects': titleProjects,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'position': user.position,
        'image': user.image,
        'projects': projects,
        'developers': developers,
        'form': form,  # Pass the form to the template
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
