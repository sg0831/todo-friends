from .serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User

# 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer