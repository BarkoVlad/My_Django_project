from rest_framework import serializers

from client.models import Purchaser


class PurchaserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchaser
        fields = ['first_name', 'second_name', 'contact', 'year', 'location', 'sex', 'role', 'size', 'phone_number']

