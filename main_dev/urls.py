from django.urls import path
from . import views

urlpatterns = [
    path('team_panel/', views.index, name='index'),
]