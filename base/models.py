import uuid as uuid
from django.db import models

from user.models import Profile


class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)

    created_at = models.DateTimeField('Дата создания', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Дата изменения', auto_now=True, editable=False)

    class Meta:
        abstract = True
