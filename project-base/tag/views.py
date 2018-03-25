from django.shortcuts import render
from rest_framework import serializers
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, IsAuthenticated


from .models import Tag
from .serializers import TagSerializer

class TagListAPIView(generics.ListAPIView):

    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Tag.objects.all()
    
class TagCreateAPIView(generics.CreateAPIView):
    
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated, )

class TagDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TagSerializer
    permission_classes = (IsAdminUser, )

    def get_queryset(self):
        queryset = Tag.objects.filter(id=self.kwargs.get('pk'))
        return queryset