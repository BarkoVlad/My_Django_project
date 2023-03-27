from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_equipment import EquipmentFilter
from equipment.api.v1.serializers.equipment_serializers import EquipmentSerializer
from equipment.models import Equipment


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EquipmentFilter
    search_fields = ['title', 'model']
    ordering_fields = ['model']