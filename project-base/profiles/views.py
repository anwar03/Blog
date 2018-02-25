from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from . import serializers
from .models import User
from .permissions import UserUpdatePermission, FeedUpdatePermission


class UserProfileViewSet(viewsets.ModelViewSet):
    """creating, reading and updating User."""

    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserUpdatePermission, IsAuthenticated)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'first_name',)


class LoginViewSet(viewsets.ViewSet):
    """Checks user email and password return auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """use the obtainAuthToken ApiView to validate and create a token."""

        return ObtainAuthToken().post(request)

'''
class FeedViewSet(viewsets.ModelViewSet):
    """Creating, reading, and updating user feed."""

    permission_classes = (FeedUpdatePermission, IsAuthenticated )
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.FeedSerializer
    queryset = UserFeed.objects.all()
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-created_on',)
    

    def perform_create(self, serializer):
        """Set the user profile to the logger in user."""

        serializer.save(user = self.request.user)


class UserBaseFeedList(viewsets.ModelViewSet):
    """feed list for only own user."""

    authentication_classes = (TokenAuthentication, )
    permission_classes = (FeedUpdatePermission, IsAuthenticatedOrReadOnly)
    serializer_class = serializers.FeedSerializer
    

    def get_queryset(self):
        queryset = UserFeed.objects.filter(user=self.request.user)
        return queryset

'''