from django_filters import rest_framework as filters

from client.models import Purchaser, PurchaserData
from core.enums.client_enums import Sex, Role


class PurchaserFilter(filters.FilterSet):
    class PurchaserFilter(filters.FilterSet):
        first_name = filters.CharFilter()
        sex = filters.ChoiceFilter(
            choices=Sex.choices,
        )
        role = filters.ChoiceFilter(
            choices=Role.choices,
        )
        year = filters.RangeFilter()

        class Meta:
            model = Purchaser
            fields = ['first_name', 'sex', 'year', 'role']


class PurchaserDataFilter(filters.FilterSet):
    value = filters.RangeFilter()

    class Meta:
        model = PurchaserData
        fields = ['value']

