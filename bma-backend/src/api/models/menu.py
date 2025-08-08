from django.db import models
from django.db.models import JSONField

class MenuModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    name = models.CharField(
        max_length=100,
        null=False
    )
    path = models.CharField(
        max_length=100,
        null=True,
        default=None
    )
    child_obj = JSONField(
        default=list
    )
    for_super_user = models.BooleanField(
        null=False,
        default=False
    )

    class Meta:
        db_table = 'menus'