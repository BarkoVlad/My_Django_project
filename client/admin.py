from django.contrib import admin, messages
from django.db.models import QuerySet

from client.models import Purchaser, PurchaserData
from core.enums.client_enums import Sex, Size, Role


@admin.register(Purchaser)
class ShopsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'contact', 'location', 'sex', 'role', 'year', 'size', 'phone_number']
    ordering = ['first_name']
    search_fields = ['first_name__istartwith']
    actions = ['change_to_sex', 'change_to_size', 'change_to_role']

    @admin.action(description='Изменить пол на женский')
    def change_to_sex(self, request, qs: QuerySet):
        updates_sex = qs.update(sex=Sex.Women)
        self.message_user(
            request,
            f'Обновлено {updates_sex} записей',
            messages.SUCCESS
        )

    @admin.action(description='Изменить размер одежды на L')
    def change_to_size(self, request, qs: QuerySet):
        updates_size = qs.update(size=Size.L)
        self.message_user(
            request,
            f'Обновлено {updates_size} записей',
            messages.SUCCESS
        )

    @admin.action(description='Изменить амплуа игрока на защитника')
    def change_to_role(self, request, qs: QuerySet):
        updates_role = qs.update(role=Role.Defender)
        self.message_user(
            request,
            f'Обновлено {updates_role} записей',
            messages.WARNING
        )


@admin.register(PurchaserData)
class PurchaserDataAdmin(admin.ModelAdmin):
    list_display = ['value', 'customer']
    ordering = ['value']
    search_fields = ['value__istartwith']


