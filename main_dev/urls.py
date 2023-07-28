from django.urls import path
from . import views

urlpatterns = [
    path('employeepanel/', views.index, name='index'),
]