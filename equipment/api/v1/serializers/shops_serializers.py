from rest_framework import serializers

from equipment.models import Shops


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = ['name', 'content', 'location', 'contact']
