from django.core.exceptions import ValidationError


def check_phonenum(phonenum):
    if len(phonenum) != 13 or phonenum[0] != '+':
        raise ValidationError('Номер введен не правильно')
