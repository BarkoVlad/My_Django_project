from rest_framework import serializers

from client.models import PurchaserData


class PurchaserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaserData
        fields = ['value', 'customer']
