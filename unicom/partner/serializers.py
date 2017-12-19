from rest_framework import serializers

from .models import Client, ApplicationForCreditor


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ApplicationForCreditorSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = ApplicationForCreditor
        fields = ('id', 'client', 'requested_credit')
