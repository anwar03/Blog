from rest_framework import serializers

from .models import Article, Comment, Reply

from profiles.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):
    """Article serializer."""
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'article']


class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer."""

    class Meta:
        model = Comment
        fields = ['id', 'article', 'created_by', 'edited', 'comment']
        extra_kwargs = {
            'edited': {'read_only': True },
            'article': {'read_only': True },
            'created_by': {'read_only': True},
            }


class CommentDetailsSerializer(serializers.ModelSerializer):
    """Comment Details serializer."""

    article = ArticleSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'article', 'created_by', 'edited', 'comment']
        extra_kwargs = {
            'edited': {'read_only': True },
            }


class ReplySerializer(serializers.ModelSerializer):
    """Reply serializer."""

    class Meta:
        model = Reply
        fields = ['id', 'reply', 'comment', 'created_by', 'created_at', 'edited']
        extra_kwargs = {
            'edited': {'read_only': True},
            'comment': { 'read_only': True },
            'created_by': { 'read_only': True },
            }


class ReplyDetailsSerializer(serializers.ModelSerializer):
    """Comment Details serializer."""

    comment = CommentSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', 'reply', 'comment', 'created_by', 'created_at', 'edited']
        extra_kwargs = {
            'edited': {'read_only': True },
            }
