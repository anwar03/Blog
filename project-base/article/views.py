from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, status, filters
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers


from . import serializers
from .models import Article, Comment, Reply
from .permissions import UpdatePermission

class ArticleList(generics.ListCreateAPIView):
    """Create and Retrun article list."""

    serializer_class = serializers.ArticleSerializer
    permisstion_classes = (IsAuthenticatedOrReadOnly, UpdatePermission)
    authentication_classes = (TokenAuthentication, )
    queryset = Article.objects.all()
    ordering = ('-created_at', )

    def perform_create(self, serializer):
        """Set the user profile to the logger in user."""
        
        serializer.save(author = self.request.user)


class CommentList(generics.ListCreateAPIView):
    """Create and Return comment list."""

    serializer_class = serializers.CommentSerializer
    permisstion_classes = (IsAuthenticatedOrReadOnly, UpdatePermission)
    authentication_classes = (TokenAuthentication, )
    queryset = Comment.objects.all()
    
    def perform_create(self, serializer):
        """Set the user profile to the logged in uesr."""
        serializer.save(created_by = self.request.user )