from django.contrib.auth import get_user_model

from dj_rest_auth.serializers import TokenSerializer
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'is_staff')
        read_only_fields = fields


class CustomTokenSerializer(TokenSerializer):
    profile = UserSerializer(many=False, read_only=True, source='user')

    class Meta(TokenSerializer.Meta):
        fields = TokenSerializer.Meta.fields + ('profile', )
