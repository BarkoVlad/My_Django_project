from django.db import models

from django_countries.fields import CountryField

from core.enums.suppliers_enums import NamePartners
from core.validators import check_phonenum


class StoresPartners(models.Model):
    name = models.CharField(max_length=255)
    contact = models.EmailField()
    location = CountryField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Магазин партнер'
        verbose_name_plural = 'Магазины партнеры'

    def __str__(self):
        return f"{self.name} {self.contact}"


class BrandPartners(models.Model):
    name_partners = models.CharField(max_length=6, choices=NamePartners.choices, default=NamePartners.CCM)
    location = CountryField()

    class Meta:
        ordering = ['name_partners']
        verbose_name = 'Название Бренда'
        verbose_name_plural = 'Названия Брендов'

    def __str__(self):
        return f"{self.name_partners} {self.location}"


class Suppliers(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, validators=[check_phonenum])
    location = CountryField()

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return f"{self.first_name} {self.phone_number}"

