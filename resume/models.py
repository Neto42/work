from django.db import models

from base.models import BaseModel
from user.models import Profile


class Resume(BaseModel):
    user = models.OneToOneField(
        Profile,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )

    text_resume = models.TextField(verbose_name='резюме')

    class Meta:
        db_table = 'resume'
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
        ordering = ['user']

    def __str__(self):
        return f"{self.user}"
