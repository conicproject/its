from django.db import models
from api.models.user import UserModel as User

class LoginModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    user = models.ForeignKey(
        User,
        null=False,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        null=False
    )
    expired_at = models.DateTimeField(
        null=False
    )

    class Meta:
        db_table = 'logins'