from django.db import models
from django.utils import timezone
from api.models.group import GroupModel as Group


class BlacklistModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    license_plate = models.CharField(
        max_length=10,
        null=True,
        default=None
    )
    plate_province = models.CharField(
        max_length=75,
        null=True,
        default=None
    )
    color = models.CharField(
        max_length=30,
        null=True,
        default=None
    )
    type =  models.CharField(
        max_length=50,
        null=True,
        default=None
    )
    note = models.CharField(
        max_length=500,
        null=True,
        default=None
    )
    date = models.DateField(
        null=False,
        default=timezone.now
    )
    group = models.ForeignKey(
        Group,
        null=True,
        default=None,
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'blacklists'
