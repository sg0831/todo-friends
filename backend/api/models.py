# User 모델 커스텀 시 필요
from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Todo( models.Model ):
	title = models.CharField( max_length=100, null=False, blank=False )
	date = models.DateTimeField( null=True )
	finished = models.BooleanField( default=False )
	user = models.ForeignKey( User, related_name='users', on_delete=models.CASCADE )
