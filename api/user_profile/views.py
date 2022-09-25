from django.shortcuts import render
from django.http import Http404
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.


class ProfileDetail(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'