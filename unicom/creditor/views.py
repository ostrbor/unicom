from rest_framework import viewsets
from django_filters import rest_framework as filters

from partner.serializers import ApplicationForCreditorSerializer
from partner.models import ApplicationForCreditor


class ApplicationReadOnlyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ApplicationForCreditorSerializer
    queryset = ApplicationForCreditor.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('status', 'client')
