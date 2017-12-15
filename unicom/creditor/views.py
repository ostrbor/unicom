from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters

from partner.serializers import ApplicationForCreditorSerializer
from partner.models import ApplicationForCreditor


class ApplicationReadOnlyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ApplicationForCreditorSerializer
    queryset = ApplicationForCreditor.objects.all()
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_fields = ('status', 'client')
    ordering_fields = ('status', 'client')

    def retrieve(self, request, *args, **kwargs):
        # TODO: check for user, must be creditor to switch status
        obj = self.get_object()
        obj.status = ApplicationForCreditor.RECEIVED
        obj.save()
        return super().retrieve(request, *args, **kwargs)
