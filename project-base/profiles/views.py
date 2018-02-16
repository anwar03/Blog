from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

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


class LoginViewSet(viewsets.ViewSet):
    """Checks user email and password return auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use the obtainAuthToken ApiView to validate and create a token."""

        return ObtainAuthToken().post(request)

