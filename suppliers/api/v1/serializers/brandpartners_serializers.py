from rest_framework import serializers

from suppliers.models import BrandPartners


class BrandPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandPartners
        fields = ['name_partners', 'location']
