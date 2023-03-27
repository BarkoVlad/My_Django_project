from django.db import models

from django_countries.fields import CountryField

from core.enums.client_enums import Sex, Role, Size
from core.validators import check_phonenum


class Purchaser(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    contact = models.EmailField()
    location = CountryField()
    sex = models.CharField(max_length=5, choices=Sex.choices, default=Sex.Men)
    role = models.CharField(max_length=10, choices=Role.choices, default=Role.Forward)
    year = models.IntegerField()
    size = models.CharField(max_length=3, choices=Size.choices, default=Size.M)
    phone_number = models.CharField(max_length=13, validators=[check_phonenum])

    class Meta:
        ordering = ['first_name']
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class PurchaserData(models.Model):
    value = models.IntegerField()
    customer = models.ForeignKey('Purchaser', on_delete=models.CASCADE)

    class Meta:
        ordering = ['value']
        verbose_name = 'Данные о покупке'
        verbose_name_plural = 'Данные о покупках'

    def __str__(self):
        return f"{self.value} {self.customer}"

