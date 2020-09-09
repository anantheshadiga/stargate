from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework.permissions import AllowAny

class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )