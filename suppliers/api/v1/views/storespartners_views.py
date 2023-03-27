from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_suppliers import StoresPartnersFilter
from suppliers.api.v1.serializers.storespartners_serializers import StoresPartnersSerializer
from suppliers.models import StoresPartners


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class StoresPartnersViewSet(viewsets.ModelViewSet):
    queryset = StoresPartners.objects.all()
    serializer_class = StoresPartnersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = StoresPartnersFilter
    search_fields = ['name', 'contact']
    ordering_fields = ['name']