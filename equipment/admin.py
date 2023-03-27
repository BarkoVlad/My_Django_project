from django.contrib import admin, messages

from django.db.models import QuerySet

from core.enums.equipment_enums import Currency, Status
from equipment.models import Equipment, Shops, Category


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'model', 'price', 'currency']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['change_to_euro']

    @admin.action(description='Изменить валюту выбранных элементов на доллары')
    def change_to_euro(self, request, qs: QuerySet):
        updates_price = qs.update(currency=Currency.USD)
        self.message_user(
            request,
            f'Обновлено {updates_price} записей',
            messages.SUCCESS
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['change_to_status']

    @admin.action(description='Изменить новую форму на Б_У')
    def change_to_status(self, request, qs: QuerySet):
        updates_status = qs.update(status=Status.B_U)
        self.message_user(
            request,
            f'Обновлено {updates_status} записей',
            messages.SUCCESS
        )


@admin.register(Shops)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ['name', 'content', 'location', 'contact']
    ordering = ['name']
    search_fields = ['name__istartwith']


