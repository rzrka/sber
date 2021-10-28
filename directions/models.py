from django.db import models
from objects.models import Objects
from entrants.models import Entrants
from uuid import uuid4


class Directions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=128)
    entrant = models.ForeignKey(Entrants, on_delete=models.DO_NOTHING)
    object = models.ForeignKey(Objects, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self) -> str:
        return self.name
