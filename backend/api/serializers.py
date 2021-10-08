from rest_framework import serializers
from .models import Todo
from django.contrib.auth.models import User

class UserSerializer( serializers.ModelSerializer ):
	class Meta:
		model = User
		fields = [ 'id', 'username', 'password' ]
		extra_kwargs = {"password" : {"write_only" : True}}


class TodoSerializer( serializers.ModelSerializer ):
	class Meta:
		model = Todo
		fields = [ 'id', 'title', 'date', 'user' ]