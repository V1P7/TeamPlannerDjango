from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.index_projects, name='index_projects'),
]