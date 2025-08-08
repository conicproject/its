from django.db import models
from django.utils import timezone
from api.models.timeRange import TimeRangeModel as TimeRange

class ViolationModel(models.Model):

    class Direction(models.TextChoices):
        in_bound = 'IN'
        out_bound = 'OUT'

    id = models.AutoField(
        primary_key=True,
        null=False
    )
    checkpoint_id = models.IntegerField(
        null=False,
        default=None
    )
    direction = models.CharField(
        max_length=3,
        choices=Direction.choices,
        default=Direction.in_bound,
    )
    car_type_id = models.IntegerField(
        null=False,
        default=None
    )
    volume = models.IntegerField(
        null=False
    )
    time_range = models.ForeignKey(
        TimeRange,
        null=False,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        null=False,
        default=timezone.now
    )
    created_at = models.DateTimeField(
        null=False,
        default=timezone.now
    )

    class Meta:
        db_table = 'violation_records'
