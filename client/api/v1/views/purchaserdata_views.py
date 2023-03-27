from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from client.api.v1.serializers.purchaserdata_serializers import PurchaserDataSerializer
from client.models import PurchaserData
from core.filters.filters_client import PurchaserDataFilter


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class PurchaserDataViewSet(viewsets.ModelViewSet):
    queryset = PurchaserData.objects.all()
    serializer_class = PurchaserDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PurchaserDataFilter
    search_fields = ['value', 'customer']
    ordering_fields = ['value']
