from rest_framework import viewsets
from partner.serializers import ApplicationForCreditorSerializer
from partner.models import ApplicationForCreditor


class ApplicationReadOnlyView(viewsets.ReadOnlyModelViewSet):
    serializer_class = ApplicationForCreditorSerializer
    queryset = ApplicationForCreditor.objects.all()
