from django.shortcuts import render
from rest_framework.response import JsonResponse
from rest_framework.views import APIView

# Create your views here.


class HelloWorld(APIView):
    def get(self, request, format=None):
        """Print 'Hello, world!' as the response body."""
        return JsonResponse("Hello, world!")
