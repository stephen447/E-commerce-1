from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.authtoken.models import Token


from .serializers import UserSerializer, LoginSerializer


# Create your views here.
class UserView(APIView):
    def post(self, request, format = 'json'):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request, format=None):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            un = serializer.data.get("username")
            pw =serializer.data.get("password")
            
            if request.user.is_authenticated:
                    return Response("Login already Sucessful", status=status.HTTP_200_OK)
            else:
                user = authenticate(request, username=un, password=pw)
                if user is not None:
                    login(request, user)
                    return Response("Login Sucessful", status=status.HTTP_200_OK)
                else: 
                    return Response("Login Unsucessful", status=status.HTTP_401_UNAUTHORIZED)
    