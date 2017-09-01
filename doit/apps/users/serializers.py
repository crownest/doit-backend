# Third-Party
from rest_framework import serializers

# Local Django
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'is_active', 'is_verify'
        )


class UserListSerializerV1(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserDetailSerializerV1(UserSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name', 'is_active', 'is_verify'
        )


class UserCreateSerializerV1(UserSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'password'
        )
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializerV1(UserSerializer):

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name'
        )
