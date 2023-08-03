from django.shortcuts import render, redirect
from django_filters.rest_framework import DjangoFilterBackend
from .models import ToDo
from accounts.models import User
from rest_framework import viewsets, filters
from .serializers import ToDoSerializzer
from .forms import ToDoForm
from datetime import datetime


# class ToDoViewSet(viewsets.ModelViewSet):
# 	queryset = ToDo.objects.all()
# 	serializer_class = ToDoSerializzer
# 	filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
# 	filterset_fields = ('title', 'user', 'is_complete')
# 	search_fields = 'title'
# 	ordering_fields = ('is_complete', 'created_at', 'updated_at')
	

def to_do_list(request):
	user, created = User.objects.get_or_create(username = request.user.username)
	form = ToDoForm()
	todos = ToDo.objects.filter(user=request.user)
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit = False)
			todo.user = request.user
			todo.save()
			return redirect('to_do_list')
	titleToDo = "open"
	context = {
		'titleToDo': titleToDo,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'position': user.position,
		'image': user.image,
		'form': form,
		'todos': todos,
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
		'form': form,
	}
	return render(request, 'to_do_list/create_to_do.html', context)


def edit_todo(request, pk):
	todo = ToDo.objects.get(pk = pk)
	if request.method == 'POST':
		form = ToDoForm(request.POST, instance = todo)
		if form.is_valid():
			form.save()
			return redirect('to_do_list')
	
	form = ToDoForm(instance = todo)
	return render(request, 'to_do_list/edit_todo.html', {'form': form})


def complete_todo(request, pk):
	todo = ToDo.objects.get(pk = pk)
	todo.is_complete = True
	todo.save()
	return redirect('to_do_list')


def delete_todo(request, pk):
	todo = ToDo.objects.get(pk = pk)
	todo.delete()
	return redirect('to_do_list')


def boss_task(request):
	titleToDo = "open"
	context = {
		'titleToDo': titleToDo,
	}
	return render(request, 'to_do_list/boss_task.html', context)