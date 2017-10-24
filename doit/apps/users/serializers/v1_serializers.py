# Local Django
from .base_serializers import (
    UserListSerializer, UserCreateSerializer,
    UserRetrieveSerializer, UserUpdateSerializer,
    UserPasswordChangeSerializer, UserPasswordForgotSerializer
)


class UserListSerializerV1(UserListSerializer):
    pass


class UserRetrieveSerializerV1(UserRetrieveSerializer):
    pass


class UserCreateSerializerV1(UserCreateSerializer):
    pass


class UserUpdateSerializerV1(UserUpdateSerializer):
    pass


class UserPasswordChangeSerializerV1(UserPasswordChangeSerializer):
    pass


class UserPasswordForgotSerializerV1(UserPasswordForgotSerializer):
	pass
