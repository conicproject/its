from django.db import models
from api.models.group import GroupModel as Group

class UserModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        null=False
    )
    password = models.CharField(
        max_length=100,
        null=False
    )
    group = models.ForeignKey(
        Group,
        null=True,
        default=None,
        on_delete=models.SET_NULL
    )
    is_super_user = models.BooleanField(
        null=False,
        default=False
    )

    class Meta:
        db_table = 'users'
