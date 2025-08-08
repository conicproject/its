from django.db import models

class TimeRangeModel(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False
    )
    start_time = models.CharField(
        max_length=5,
        null=False
    )
    end_time = models.CharField(
        max_length=5,
        null=False
    )

    class Meta:
        db_table = 'time_ranges'