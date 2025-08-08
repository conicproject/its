from django.db import models
from api.models.group import GroupModel as Group
from api.models.menu import MenuModel as Menu

class PermissionModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    group = models.ForeignKey(
        Group,
        null=True,
        default=None,
        on_delete=models.SET_NULL
    )
    menu = models.ForeignKey(
        Menu,
        null=True,
        default=None,
        on_delete=models.SET_NULL
    )

    class Meta:
        db_table = 'permissions'
