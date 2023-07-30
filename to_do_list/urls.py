from django.urls import path
from . import views

urlpatterns = [
	path('to_do_list/', views.to_do_list, name = 'to_do_list'),
]
