from django.db import models
from django.conf import settings
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
	