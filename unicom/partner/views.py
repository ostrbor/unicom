from rest_framework import viewsets, mixins
from .serializers import ClientSerializer, ApplicationForCreditorSerializer
from .models import Client, ApplicationForCreditor


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ApplicationCreateView(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    queryset = ApplicationForCreditor.objects.all()
    serializer_class = ApplicationForCreditorSerializer
