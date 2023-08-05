from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index_projects, name='index_projects'),
    path('create_project/', views.create_project, name='create_project'),
]