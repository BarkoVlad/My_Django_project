from rest_framework import serializers

from suppliers.models import Suppliers


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ['first_name', 'second_name', 'phone_number', 'location']
