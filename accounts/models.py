from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	age = models.PositiveIntegerField(null = True, blank = True)
	birthday = models.DateField(null = True, blank = True)
	position = models.CharField(max_length = 20)
	join_date = models.DateField(null = True, blank = True)
	image = models.ImageField(upload_to='media', blank=True, default='media/avatar.png')
	is_on_leave = models.BooleanField(default = False)
	
	def __str__(self):
		return self.username
