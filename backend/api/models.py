# User 모델 커스텀 시 필요
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class Todo_list( models.Model ):
	title = models.CharField( max_length=100 )
	date = models.DateTimeField( null=True )
	check = models.BooleanField( default=True )
	user = models.ForeignKey( User, related_name='users' ,on_delete=models.CASCADE )
