from django.shortcuts import render
from rest_framework import generics, views, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserModel
from .serializers import UserSerializer


class RegisterView(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class BlacklistRefreshView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        return Response("Success")