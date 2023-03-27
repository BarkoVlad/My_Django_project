from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from client.api.v1.serializers.purchaser_serializers import PurchaserSerializer
from client.models import Purchaser
from core.filters.filters_client import PurchaserFilter


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class PurchaserViewSet(viewsets.ModelViewSet):
    queryset = Purchaser.objects.all()
    serializer_class = PurchaserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaserFilter
    search_fields = ['first_name', 'role']
    ordering_fields = ['first_name']