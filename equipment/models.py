from django.db import models

from django_countries.fields import CountryField

from core.enums.equipment_enums import Currency, Model, Brand, Status


class Equipment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    model = models.CharField(max_length=15, choices=Model.choices, default=Model.Stick)
    brand = models.CharField(max_length=6, choices=Brand.choices, default=Brand.CCM)
    price = models.IntegerField(default=100)
    currency = models.CharField(max_length=3, choices=Currency.choices, default=Currency.RUB)

    class Meta:
        ordering = ['title']
        verbose_name = 'Экиперовка'
        verbose_name_plural = 'Экиперовка'

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=5, choices=Status.choices, default=Status.New)

    class Meta:
        ordering = ['status']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f"{self.title} {self.status}"


class Shops(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    location = CountryField()
    contact = models.EmailField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'

    def __str__(self):
        return f"{self.name} {self.location}"


