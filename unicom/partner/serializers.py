from rest_framework import serializers

from .models import Client, ApplicationForCreditor


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ApplicationForCreditorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ApplicationForCreditor
        fields = '__all__'
