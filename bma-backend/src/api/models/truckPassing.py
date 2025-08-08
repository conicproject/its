from django.db import models


class TruckPassingModel(models.Model):
    pass_id = models.CharField(
        max_length=64,
        null=True
    )
    plate_url = models.CharField(
        max_length=200,
        null=True
    )
    image_url = models.CharField(
        max_length=200,
        null=True
    )
    plate_no = models.CharField(
        max_length=20,
        null=True
    )
    province = models.CharField(
        max_length=50,
        null=True      
    )
    checkpoint = models.CharField(
        max_length=80,
        null=True      
    )
    latitude = models.CharField(
        max_length=12,
        null=True
    )
    longtitude = models.CharField(
        max_length=12,
        null=True
    )
    direction = models.CharField(
        max_length=12,
        null=True
    )
    pass_time = models.DateTimeField(
        null=True
    )
    type = models.CharField(
        max_length=24,
        null=True
    )
    color = models.CharField(
        max_length=12,
        null=True
    )
    rtsp_url =  models.CharField(
        max_length=200,
        null=True
    )

    class Meta:
        db_table = 'trucks_passing'