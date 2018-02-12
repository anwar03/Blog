from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Return a list of Api view."""

        an_apiview = [
            'Uses HTTP method as function (GET, POST, PUT, PATCH, DELETE)'
        ]

        return Response({'message': 'Hello world!', 'an_apiview': an_apiview })
