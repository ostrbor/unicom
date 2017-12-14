from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, ApplicationForCreditorSerializer
from .models import Client, ApplicationForCreditor


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = ApplicationForCreditor.objects.all()
    serializer_class = ApplicationForCreditorSerializer
