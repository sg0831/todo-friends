from rest_framework import serializers
from .models import Todo_list
from django.contrib.auth.models import User

class UserSerializer( serializers.ModelSerializer ):
	class Meta:
		model = User
		fields = [ 'username', 'password' ]
		extra_kwargs = {"password" : {"write_only" : True}}
