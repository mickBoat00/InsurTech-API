from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class signup(APIView):
    def post(self, request, format=None):

        email = request.data.get("email")
        password = request.data.get("password")
        user = User.objects.create_user(username=email, email=email, password=password, is_superuser=True, is_staff=True)
        token = Token.objects.create(user=user)

        response = {
            "email": user.email,
            "token": token.key
        }

        return Response(response)