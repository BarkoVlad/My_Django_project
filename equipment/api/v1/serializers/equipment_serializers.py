from rest_framework import serializers

from equipment.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['title', 'content', 'model', 'brand', 'price', 'currency']
