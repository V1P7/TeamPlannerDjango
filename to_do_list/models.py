from django.db import models
from accounts.models import User


class ToDo(models.Model):
	title = models.CharField(max_length = 64, null = False)
	description = models.TextField(null = True)
	is_complete = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'todo', null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	deadline = models.DateTimeField()
	
	def __str__(self):
		return self.title


class BossTask(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField()
	is_complete = models.BooleanField(default = False)
	deadline = models.DateTimeField(blank = True, null=True)
	date = models.DateTimeField(blank = True, null=True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.title