from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class signup(APIView):
    def post(self, request, format=None):
        try:
            email = request.data.get("email")
            password = request.data.get("password")
            user = User.objects.create_user(username=email, email=email, password=password, is_superuser=True, is_staff=True)
            token = Token.objects.create(user=user)

            response = {
                "email": user.email,
                "token": token.key
            }

            return Response(response)
        except Exception as e:
            return Response({'error': str(e)})


class login(APIView):
    def post(self, request, format=None):
        try:

            email = request.data.get("email")
            password = request.data.get("password")

            user = authenticate(username=email, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"token": token.key})

            return Response({"error": "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'error': str(e)})
    

class logout(APIView):
    def post(self, request, format=None):
        try:
            self.request.user.auth_token.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)})
