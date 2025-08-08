from rest_framework import serializers
from api.models.blacklist import BlacklistModel


class BlacklistSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlacklistModel
        fields = '__all__'