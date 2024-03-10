from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.renderers import JSONRenderer


class GreetingApi(APIView):
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        return Response({"message": "Hello world"})

# Create your views here.
