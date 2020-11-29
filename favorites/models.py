from django.db import models

from hh_site.models import Ad
from user.models import Profile


class Favorites(models.Model):
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )

    ad = models.ForeignKey(
        Ad,
        verbose_name='Объявление',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'
        ordering = ['user']

    def __str__(self):
        return f"{self.ad}"
