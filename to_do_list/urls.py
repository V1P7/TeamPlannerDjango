from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('api/todo', views.ToDoViewSet, basename = 'todo')
# urlpatterns = router.urls

urlpatterns = [
	path('to_do_list/', views.to_do_list, name = 'to_do_list'),
	path('create_to_do/', views.create_to_do, name = 'create_to_do'),
	path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo'),
	path('complete_todo/<int:pk>/', views.complete_todo, name='complete_todo'),
	path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
	path('boss_task/', views.boss_task, name='boss_task'),
	path('edit_boss_task/<int:pk>/', views.edit_boss_task, name='edit_boss_task'),
	path('complete_boss_task/<int:pk>/', views.complete_boss_task, name='complete_boss_task'),
	path('delete_boss_task/<int:pk>/', views.delete_boss_task, name='delete_boss_task'),
	path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
