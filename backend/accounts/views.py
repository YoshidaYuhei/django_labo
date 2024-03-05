from django.shortcuts import render
from .models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]