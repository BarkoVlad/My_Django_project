from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filters.filters_equipment import CategoryFilter
from equipment.api.v1.serializers.category_serializers import CategorySerializer
from equipment.models import Category


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
    search_fields = ['title', 'status']
    ordering_fields = ['title']