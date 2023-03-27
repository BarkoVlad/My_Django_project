from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_suppliers import BrandPartnersFilter
from suppliers.api.v1.serializers.brandpartners_serializers import BrandPartnersSerializer
from suppliers.models import BrandPartners


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class BrandPartnersViewSet(viewsets.ModelViewSet):
    queryset = BrandPartners.objects.all()
    serializer_class = BrandPartnersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BrandPartnersFilter
    search_fields = ['name_partners', 'location']
    ordering_fields = ['name_partners']