from django.contrib import admin, messages
from django.db.models import QuerySet

from core.enums.suppliers_enums import NamePartners
from suppliers.models import StoresPartners, BrandPartners, Suppliers


@admin.register(StoresPartners)
class StoresPartnersAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'location']
    ordering = ['name']
    search_fields = ['name__istartwith']


@admin.register(BrandPartners)
class BrandPartnersAdmin(admin.ModelAdmin):
    list_display = ['name_partners', 'location']
    ordering = ['name_partners']
    search_fields = ['name_partners__istartwith']
    actions = ['change_to_partners']

    @admin.action(description='Изменить название фирмы CCM на Bauer')
    def change_to_partners(self, request, qs: QuerySet):
        updates_partners = qs.update(namepartners=NamePartners.Bauer)
        self.message_user(
            request,
            f'Обновлено {updates_partners} записей',
            messages.SUCCESS
        )


@admin.register(Suppliers)
class SuppliersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'phone_number', 'location']
    ordering = ['first_name']
    search_fields = ['first_name__istartwith']