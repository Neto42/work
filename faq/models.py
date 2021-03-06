from django.db import models

from base.models import BaseModel
from user.models import Profile


class Question(BaseModel):
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    theme = models.CharField(verbose_name='Тема', max_length=50)
    text = models.TextField(verbose_name='Вопрос')

    class Meta:
        db_table = 'question'
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['user']

    def __str__(self):
        return f"{self.theme}"


class Answer(BaseModel):
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    quest = models.OneToOneField(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )

    theme = models.CharField(verbose_name='Тема', max_length=50)
    text = models.TextField(verbose_name='Ответ')

    class Meta:
        db_table = 'answer'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['user']

    def __str__(self):
        return f"{self.theme}"
