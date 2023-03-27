from django.db import models


class Currency(models.TextChoices):
    EUR = 'EUR', 'EUR'
    USD = 'USD', 'USD'
    RUB = 'RUB', 'RUB'


class Model(models.TextChoices):
    Stick = 'Stick', 'Stick'
    Hockey_skates = 'Hockey_skates', 'Hockey_skates'
    Gloves = 'Gloves', 'Gloves'
    Knee_pad = 'Knee_pad', 'Knee_pad'
    Shoulder_pad = 'Shoulder_pad', 'Shoulder_pad'
    Helmet = 'Helmet', 'Helmet'
    Puck = 'Puck', 'Puck'
    Chest_pad = 'Chest_pad', 'Chest_pad'


class Status(models.TextChoices):
    New = 'New', 'New'
    B_U = 'B_U', 'B_U'


class Brand(models.TextChoices):
    Bauer = 'Bauer', 'Bauer'
    Reebok = 'Reebok', 'Reebok'
    Easton = 'Easton', 'Easton'
    CCM = 'CCM', 'CCM'
    FISHER = 'FISHER', 'FISHER'