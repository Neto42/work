from django.db import models

from base.models import BaseModel
from faq.models import Question, Answer
from hh_site.models import Ad
from organization.models import Organization
from user.models import Profile


class CommentAd(BaseModel):
    ad = models.ForeignKey(
        Ad,
        verbose_name='Объявление',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(verbose_name='Комментарий')

    class Meta:
        db_table = 'comment_ad'
        verbose_name = 'Комментарий для объявлений'
        verbose_name_plural = 'Комментарии для объявлений'
        ordering = ['ad']

    def __str__(self):
        return f"{self.ad}: {self.user}"


class CommentOrganization(BaseModel):
    organization = models.ForeignKey(
        Organization,
        verbose_name='Организация',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(verbose_name='Комментарий')

    class Meta:
        db_table = 'comment_organization'
        verbose_name = 'Комментарий для организации'
        verbose_name_plural = 'Комментарии для оорганизаций'
        ordering = ['organization']

    def __str__(self):
        return f"{self.organization}: {self.user}"


class CommentQuestion(BaseModel):
    quest = models.ForeignKey(
        Question,
        verbose_name='Вопрос',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(verbose_name='Комментарий')

    class Meta:
        db_table = 'comment_question'
        verbose_name = 'Комментарий для вопроса'
        verbose_name_plural = 'Комментарии для вопросов'
        ordering = ['quest']

    def __str__(self):
        return f"{self.quest}: {self.user}"


class CommentAnswer(BaseModel):
    answer = models.ForeignKey(
        Answer,
        verbose_name='Ответ',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        Profile,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    comment_text = models.TextField(verbose_name='Комментарий')

    class Meta:
        db_table = 'comment_answer'
        verbose_name = 'Комментарий для ответа'
        verbose_name_plural = 'Комментарии для ответов'
        ordering = ['answer']

    def __str__(self):
        return f"{self.answer}: {self.user}"
