from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# router = DefaultRouter()
# router.register('api/todo', views.ToDoViewSet, basename = 'todo')
# urlpatterns = router.urls

urlpatterns = [
	path('to_do_list/', views.to_do_list, name = 'to_do_list'),
	path('create/', views.create_todo, name = 'create_to_do'),
]
