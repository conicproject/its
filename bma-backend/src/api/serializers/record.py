from rest_framework import serializers
from api.models.record import RecordModel

class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecordModel
        fields = '__all__'