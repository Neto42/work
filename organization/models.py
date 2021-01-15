from django.core.validators import RegexValidator
from django.db import models

from base.models import BaseModel


class Organization(BaseModel):
    organization = models.CharField(
        verbose_name='Организация',
        max_length=50,
    )

    inn = models.CharField(
        max_length=9,
        verbose_name='ИНН',
        unique=True,
        validators=[RegexValidator(regex='^[0-9]{9}$', message='Введите корректный ИНН', code='nomatch')]
    )

    kpp = models.CharField(
        max_length=11,
        verbose_name='КПП',
        unique=True,
        validators=[RegexValidator(regex='^[0-9]{11}$', message='Введите корректный КПП', code='nomatch')]
    )

    ogrn = models.CharField(
        max_length=10,
        verbose_name='ОГРН',
        unique=True,
        validators=[RegexValidator(regex='^[0-9]{10}$', message='Введите корректный ОГРН', code='nomatch')]
    )

    image = models.ImageField(verbose_name='Логотип организации', null=True, blank=True)
    text_org = models.TextField(verbose_name='Описание организации')
    link = models.CharField(verbose_name='Ссылка на сайт организации', max_length=50, null=True, blank=True)
    email = models.EmailField(verbose_name='Почта организации')

    class Meta:
        db_table = 'organization'
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return f"{self.organization}"
