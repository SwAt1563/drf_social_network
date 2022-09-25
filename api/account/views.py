from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from .models import UserAccount
from django.conf import settings
# Create your views here.


class RegisterUserAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
