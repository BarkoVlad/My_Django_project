from django_filters import rest_framework as filters

from core.enums.equipment_enums import Brand, Model, Currency, Status
from equipment.models import Equipment, Category, Shops


class EquipmentFilter(filters.FilterSet):
    title = filters.CharFilter()
    price = filters.RangeFilter()
    model = filters.ChoiceFilter(
        choices=Model.choices,
    )
    brand = filters.ChoiceFilter(
        choices=Brand.choices,
    )
    currency = filters.ChoiceFilter(
        choices=Currency.choices,
    )

    class Meta:
        model = Equipment
        fields = ['title', 'price', 'model', 'brand']


class CategoryFilter(filters.FilterSet):
    title = filters.CharFilter()
    status = filters.ChoiceFilter(
        choices=Status.choices,
    )

    class Meta:
        model = Category
        fields = ['title', 'status']


class ShopsFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Shops
        fields = ['name']
