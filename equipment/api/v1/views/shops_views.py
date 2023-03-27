from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_equipment import ShopsFilter
from equipment.api.v1.serializers.shops_serializers import ShopsSerializer
from equipment.models import Shops


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class ShopsViewSet(viewsets.ModelViewSet):
    queryset = Shops.objects.all()
    serializer_class = ShopsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ShopsFilter
    search_fields = ['name', 'location']
    ordering_fields = ['name']