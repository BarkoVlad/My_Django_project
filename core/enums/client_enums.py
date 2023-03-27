from django.db import models


class Sex(models.TextChoices):
    Men = 'Men', 'Men'
    Women = 'Women', 'Women'


class Role(models.TextChoices):
    Forward = 'Forward', 'Forward'
    Defender = 'Defender', 'Defender'
    GoalKeeper = 'GoalKeeper', 'GoalKeeper'


class Size(models.TextChoices):
    XS = 'XS', 'XS'
    S = 'S', 'S'
    M = 'M', 'M'
    L = 'L', 'L'
    XL = 'XL', 'XL'
    XXL = 'XXL', 'XXL'