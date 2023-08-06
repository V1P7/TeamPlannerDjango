from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index_projects, name='index_projects'),
    path('create_project/', views.create_project, name='create_project'),
    path('edit_project/<int:pk>/', views.edit_project, name='edit_project'),
	path('complete_project/<int:pk>/', views.complete_project, name='complete_project'),
	path('delete_project/<int:pk>/', views.delete_project, name='delete_project'),
]