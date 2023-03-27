from django_filters import rest_framework as filters

from suppliers.models import StoresPartners, BrandPartners, Suppliers


class StoresPartnersFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = StoresPartners
        fields = ['name']


class BrandPartnersFilter(filters.FilterSet):
    name_partners = filters.CharFilter()

    class Meta:
        model = BrandPartners
        fields = ['name_partners']


class SuppliersFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    second_name = filters.CharFilter()

    class Meta:
        model = Suppliers
        fields = ['first_name', 'second_name']
