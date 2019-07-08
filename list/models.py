from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
	id = models.AutoField(primary_key=True)
	time_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	title = models.CharField(max_length = 500, blank = False, null = True)
	description = models.TextField(max_length = 1000, blank = False, null = True)
	user_created = models.ForeignKey(User, related_name ="%(app_label)s_%(class)s_related_modified",editable = False, null=True, blank=True,on_delete=models.CASCADE,)
	time_modified = models.DateTimeField(auto_now=True, null=True, blank=True)
	is_delete = models.BooleanField(default=False)
	status = models.CharField(choices = (
	('in_progress', 'In Progress'),
	('completed', 'Completed'),
	('pending', 'Pending'),

	), max_length = 50,blank = True,null = True)

