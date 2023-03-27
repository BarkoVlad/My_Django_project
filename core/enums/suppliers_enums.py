from django.db import models


class NamePartners(models.TextChoices):
    Bauer = 'Bauer', 'Bauer'
    Reebok = 'Reebok', 'Reebok'
    Easton = 'Easton', 'Easton'
    CCM = 'CCM', 'CCM'
    FISHER = 'FISHER', 'FISHER'
