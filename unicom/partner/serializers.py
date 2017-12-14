from rest_framework import serializers

from .models import Client, ApplicationForCreditor


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ApplicationForCreditorSerializer(serializers.ModelSerializer):
    client = ClientSerializer()

    class Meta:
        model = ApplicationForCreditor
        fields = '__all__'
