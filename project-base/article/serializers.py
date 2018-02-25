from rest_framework import serializers

from .models import Article, Comment, Reply

from profiles.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer."""
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'article']
        #extra_kwargs = {'author': {'read_only': True }}


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer."""

    article = ArticleSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'created_by', 'edited', 'comment']
        extra_kwargs = {'edited': {'read_only': True }}