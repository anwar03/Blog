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
    #authentication_classes = (TokenAuthentication, )
    queryset = Article.objects.all()
    ordering = ('-created_at', )

    def perform_create(self, serializer):
        """Set the user profile to the logger in user."""
        
        serializer.validated_data['author'] = self.request.user
        return super(ArticleList, self).perform_create(serializer)


class ArticleDetails(generics.RetrieveUpdateDestroyAPIView):
    
    permisstion_classes = (UpdatePermission, IsAuthenticatedOrReadOnly)
    serializer_class = serializers.ArticleDetailSerializer
    queryset = Article.objects.filter()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    


class CommentList(generics.ListCreateAPIView):
    """Create and Return comment list."""

    serializer_class = serializers.CommentSerializer
    permisstion_classes = (IsAuthenticatedOrReadOnly, UpdatePermission)
    #authentication_classes = (TokenAuthentication, )
    queryset = Comment.objects.filter()
    lookup_field = 'pk'
    
    def perform_create(self, serializer):
        """Set the user profile to the logged in uesr."""
        
        self.article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        print('article: ', self.article)
        serializer.validated_data['article'] = self.article
        serializer.validated_data['created_by'] = self.request.user
        return super(CommentList, self).perform_create(serializer)