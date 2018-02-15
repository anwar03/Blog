from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from . import serializers
from .models import User

class UserProfileViewSet(viewsets.ModelViewSet):
    """creating, reading and updating User."""

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
