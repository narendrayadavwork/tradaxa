from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):	
	title = models.CharField(max_length=256)
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True, null=True)
	updated = models.DateTimeField(auto_now=True, null=True)

	def __str__(self):
		return self.title



# Post : user, text, created_at, updated_at