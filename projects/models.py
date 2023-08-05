from django.db import models
from accounts.models import User


class Project(models.Model):
	title_name = models.CharField(max_length = 100)
	description = models.TextField()
	is_complete = models.BooleanField(default = False)
	deadline = models.DateTimeField(blank = True, null = True)
	created_at = models.DateTimeField(auto_now_add = True)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	developers = models.ManyToManyField(User, related_name = 'projects', blank = True)
	
	def __str__(self):
		return self.title_name
