from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_suppliers import SuppliersFilter
from suppliers.api.v1.serializers.suppliers_serializers import SuppliersSerializer
from suppliers.models import Suppliers


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class SuppliersViewSet(viewsets.ModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SuppliersFilter
    search_fields = ['first_name', 'phone_number']
    ordering_fields = ['first_name']