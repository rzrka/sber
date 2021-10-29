from django.db import models
from uuid import uuid4

from objects.models import Objects


class Entrants(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    middlename = models.CharField(max_length=64)
    birthday = models.DateField()
    pass_number = models.IntegerField()
    pass_series = models.IntegerField()
    subject = models.ForeignKey(Objects, on_delete=models.DO_NOTHING)
    mark = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Поступающий'
        verbose_name_plural = 'Поступающие'

    def __str__(self) -> str:
        return f"{self.name} {self.surname} {self.middlename}"
