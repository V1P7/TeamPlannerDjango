from django.shortcuts import render, redirect
from .models import ToDo, BossTask
from accounts.models import User
from projects.models import Project
from .forms import ToDoForm, BossTaskForm
from main_dev.views import get_vacation_days


def to_do_list(request):
	user, created = User.objects.get_or_create(username = request.user.username)
	tasks = BossTask.objects.filter(user = request.user)
	todos = ToDo.objects.filter(user=request.user)
	projects = Project.objects.filter(developers = request.user)
	vacation_days = get_vacation_days(request)
	titleToDo = "open"
	context = {
		'titleToDo': titleToDo,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'todos': todos,
		'tasks': tasks,
		'projects': projects,
		'vacation_days': vacation_days,
	}
	return render(request, 'to_do_list/index.html', context)


def create_to_do(request):
	user, created = User.objects.get_or_create(username = request.user.username)
	form = ToDoForm()
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit = False)
			todo.user = request.user
			todo.save()
			return redirect('to_do_list')
		
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form': form,
	}
	return render(request, 'to_do_list/create_to_do.html', context)


def edit_todo(request, pk):
	user, created = User.objects.get_or_create(username = request.user.username)
	todo = ToDo.objects.get(pk = pk)
	if request.method == 'POST':
		form = ToDoForm(request.POST, instance = todo)
		if form.is_valid():
			form.save()
			return redirect('to_do_list')
	
	form = ToDoForm(instance = todo)
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form': form,
	}
	return render(request, 'to_do_list/edit_todo.html', context)


def complete_todo(request, pk):
	todo = ToDo.objects.get(pk = pk)
	todo.is_complete = True
	todo.save()
	return redirect('to_do_list')


def delete_todo(request, pk):
	todo = ToDo.objects.get(pk = pk)
	todo.delete()
	return redirect('to_do_list')


def boss_task(request): # create boss task
	user, created = User.objects.get_or_create(username = request.user.username)
	tasks = BossTask.objects.filter()
	form2 = BossTaskForm()
	if request.method == 'POST':
		form2 = BossTaskForm(request.POST)
		if form2.is_valid():
			task = form2.save()
			return redirect('boss_task')
		
	vacation_days = get_vacation_days(request)
	titleAllTasks = "open"
	context = {
		'titleAllTasks': titleAllTasks,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'tasks': tasks,
		'form2': form2,
		'vacation_days': vacation_days,
	}
	return render(request, 'to_do_list/boss_task.html', context)


def edit_boss_task(request, pk):
	user, created = User.objects.get_or_create(username = request.user.username)
	task = BossTask.objects.get(pk = pk)
	if request.method == 'POST':
		form2 = BossTaskForm(request.POST, instance = task)
		if form2.is_valid():
			form2.save()
			return redirect('boss_task')
	
	form2 = BossTaskForm(instance = task)
	context = {
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form2': form2,
	}
	return render(request, 'to_do_list/edit_boss_task.html', context)


def complete_boss_task(request, pk):
	task = BossTask.objects.get(pk = pk)
	task.is_complete = True
	task.save()
	return redirect('to_do_list')


def delete_boss_task(request, pk):
	task = BossTask.objects.get(pk = pk)
	task.delete()
	return redirect('boss_task')


def delete_task(request, pk):
	task = BossTask.objects.get(pk = pk)
	task.delete()
	return redirect('to_do_list')