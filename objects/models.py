from django.db import models
from uuid import uuid4


class Objects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128)
    mark = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self) -> str:
        return self.name
