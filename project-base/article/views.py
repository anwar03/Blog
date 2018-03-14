from django.shortcuts import render, get_object_or_404
from rest_framework import generics, viewsets, status, filters
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import serializers


from . import serializers
from .models import Article, Comment, Reply
from .permissions import ArticleUpdatePermission, CommentUpdatePermission, ReplyUpdatePermission

class ArticleListAPIView(generics.ListCreateAPIView):
    """Create and Retrun article list."""

    serializer_class = serializers.ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication, )
    queryset = Article.objects.all()

    def perform_create(self, serializer):
        """Set the user profile to the logger in user."""
        
        serializer.validated_data['author'] = self.request.user
        return super(ArticleListAPIView, self).perform_create(serializer)


class ArticleDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = (ArticleUpdatePermission, IsAuthenticatedOrReadOnly)
    serializer_class = serializers.ArticleDetailsSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class CommentListAPIView(generics.ListCreateAPIView):
    """Create and Return comments list."""

    serializer_class = serializers.CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication, )
    
    def get_queryset(self):
        queryset = Comment.objects.filter(article_id=self.kwargs.get('pk'))
        return queryset

    def perform_create(self, serializer):
        """Set the user profile to the logged in uesr and define article."""
        
        self.article = Article.objects.get(id=self.kwargs.get('pk'))
        serializer.validated_data['article'] = self.article
        serializer.validated_data['created_by'] = self.request.user
        return super(CommentListAPIView, self).perform_create(serializer)


class CommentDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Delete Comment."""

    serializer_class = serializers.CommentDetailsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, CommentUpdatePermission)

    def get_queryset(self):
        queryset = Comment.objects.filter(id=self.kwargs.get('pk'))
        return queryset


class ReplyListAPIView(generics.ListCreateAPIView):
    """Create and return comment's reply List."""

    serializer_class = serializers.ReplySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        queryset = Reply.objects.filter(comment_id=self.kwargs.get('pk'))
        return queryset

    
    def perform_create(self, serializer):
        self.comment = Comment.objects.get(id=self.kwargs.get('pk'))
        serializer.validated_data['comment'] = self.comment
        serializer.validated_data['created_by'] = self.request.user
        return super(ReplyListAPIView, self).perform_create(serializer)


class ReplyDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, Update and Delete Comment."""

    serializer_class = serializers.ReplyDetailsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, ReplyUpdatePermission)

    def get_queryset(self):
        queryset = Reply.objects.filter(id=self.kwargs.get('pk'))
        return queryset

