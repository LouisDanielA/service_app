from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer
class ClientAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
