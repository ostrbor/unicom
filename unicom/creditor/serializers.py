from rest_framework import serializers

from partner.models import Client, ApplicationForCreditor


class ApplicationForCreditorSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = ApplicationForCreditor
        fields = '__all__'
