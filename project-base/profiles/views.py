from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters


from . import serializers
from .models import User
from .permissions import UserUpdatePermission


class UserProfileViewSet(viewsets.ModelViewSet):
    """creating, reading and updating User."""

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    authetication_classes = (TokenAuthentication,)
    permission_classes = (UserUpdatePermission, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'first_name',)