from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

from user.models import ModelForCeleryTest

CustomUser = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'password', 'is_active', 'role', 'date_joined', 'last_login')
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            'is_active': {'read_only': True},
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)


class CustomUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class ModelForCeleryTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelForCeleryTest
        fields = '__all__'
