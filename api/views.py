from .serializers import UserSerializer, TodoSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Todo
from rest_framework.decorators import action
from rest_framework.response import Response


# 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

	@action( detail=True )
	def todo_list_of_user( self, request, pk ):
		qs = self.queryset.filter( user=pk ).order_by('date')
		serializer = self.get_serializer( qs, many=True )
		return Response( serializer.data )