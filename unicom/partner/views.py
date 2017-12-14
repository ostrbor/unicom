from rest_framework import viewsets, mixins
from django_filters import rest_framework as filters

from .serializers import ClientSerializer, ApplicationForCreditorSerializer
from .models import Client, ApplicationForCreditor


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'surname')


class ApplicationCreateView(mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    # TODO: why set queryset for Create only view if there is model serializer?
    queryset = ApplicationForCreditor.objects.none()
    serializer_class = ApplicationForCreditorSerializer
