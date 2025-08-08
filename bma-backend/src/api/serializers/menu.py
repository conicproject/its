from rest_framework import serializers
from api.models.menu import MenuModel

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuModel
        exclude = ['for_super_user']