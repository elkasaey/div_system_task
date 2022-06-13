from rest_framework import serializers
from user.models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer ,RefreshToken


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):

        password = validated_data.pop('password', '')


        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password:
            instance.set_password(password)

        instance.save()

        return instance


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']

class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['phone_number'] = str(user.phone_number)
        return token
