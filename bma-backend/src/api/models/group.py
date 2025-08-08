from django.db import models

class GroupModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False
    )

    class Meta:
        db_table = 'groups'