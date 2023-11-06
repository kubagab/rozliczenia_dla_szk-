import datetime

from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rozliczenia_dla_szkół import settings
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import jwt
import secrets


# Create your views here.
class RegisterAPI(APIView):
    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=request.data['username'],
                password=request.data['password'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )
            if user:
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)  # Generate a refresh token
            access_token = refresh.access_token

            response = Response()
            response.set_cookie(key='jwt', value=str(access_token), httponly=True)
            response.data = {
                'jwt': str(access_token),
                'refresh_token': str(refresh)
            }
            return response
    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         refresh = RefreshToken.for_user(user)
    #         access_token = str(refresh.access_token)
    #         return Response({'access_token': access_token})
    #     else:
    #         return Response({'message': 'Nieprawidłowe dane logowania.'})
    # def post(self, request):
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #
    #     user = authenticate(username=username, password=password)
    #
    #     if user is not None:
    #         login(request, user)
    #         payload = {
    #             'user_id': user.id,
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
    #             'iat': datetime.datetime.utcnow()
    #         }
    #         token = jwt.encode(payload, 'settings.SECRET_KEY', algorithm='HS256')
    #         response = Response()
    #         response.set_cookie(key='jwt', value=token, httponly=True)
    #         response.data = {
    #             'jwt': token
    #         }
    #         return response


class UserAPI(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        payload = jwt.decode(token, 'settings.SECRET_KEY', algorithms='HS256')
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer
        return Response(token)