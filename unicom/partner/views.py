from rest_framework import viewsets, mixins, generics, serializers
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.response import Response

from .serializers import ClientSerializer, ApplicationForCreditorSerializer
from .models import Client, ApplicationForCreditor
from .permissions import AccessToPartnerApi


class ClientViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filter_fields = ('name', 'surname')
    ordering_fields = ('surname', 'credit_score')
    permission_classes = (AccessToPartnerApi,)


class ApplicationCreateView(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    # TODO: why set queryset for Create only view if there is model serializer?
    queryset = ApplicationForCreditor.objects.all()
    serializer_class = ApplicationForCreditorSerializer
    permission_classes = (AccessToPartnerApi,)


class ApplicationSendView(generics.GenericAPIView):
    queryset = ApplicationForCreditor.objects.all()
    serializer_class = serializers.Serializer  # no need in serializer, use dummy
    permission_classes = (AccessToPartnerApi,)

    def patch(self, request, *args, **kwargs):
        '''
        Automatically patch one field in application model.
        '''
        instance = self.get_object()
        instance.status = ApplicationForCreditor.SENT
        instance.save()
        return Response({'Result': 'Application was successfully sent to creditor.'})
