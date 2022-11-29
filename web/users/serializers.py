from django.contrib.auth import get_user_model

from dj_rest_auth.serializers import TokenSerializer, UserDetailsSerializer
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.URLField(source='userprofile.avatar', read_only=True)

    class Meta:
        model = UserModel
        fields = ('id', 'username', 'is_staff', 'avatar')
        read_only_fields = fields


class CustomTokenSerializer(TokenSerializer):
    profile = UserSerializer(many=False, read_only=True, source='user')

    class Meta(TokenSerializer.Meta):
        fields = TokenSerializer.Meta.fields + ('profile', )


class CustomUserDetailSerializer(UserDetailsSerializer):
    avatar = serializers.URLField(source='userprofile.avatar', read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('avatar', 'date_joined', 'is_staff')


class UserOutputFilterSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)


class UserOutputSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    avatar = serializers.URLField(source='userprofile.avatar', read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    is_staff = serializers.BooleanField()


class UserDetailOutputSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    avatar = serializers.URLField(source='userprofile.avatar', read_only=True)
    date_joined = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    is_staff = serializers.BooleanField()
