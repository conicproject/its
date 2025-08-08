from rest_framework import serializers
from api.models.login import LoginModel

class LoginSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LoginModel
        fields = ['id', 'user_id', 'created_at']


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = LoginModel
        fields = '__all__'