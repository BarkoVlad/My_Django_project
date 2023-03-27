from rest_framework import serializers

from suppliers.models import StoresPartners


class StoresPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoresPartners
        fields = ['name', 'contact', 'location']
