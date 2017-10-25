# Local Django
from .base_serializers import (
    UserSerializer, UserListSerializer, UserCreateSerializer,
    UserRetrieveSerializer, UserUpdateSerializer, UserImageUpdateSerializer,
    UserPasswordChangeSerializer, UserPasswordForgotSerializer,
    UserActivationResendSerializer
)
from .v1_serializers import (
    UserListSerializerV1, UserCreateSerializerV1,
    UserRetrieveSerializerV1, UserUpdateSerializerV1, UserImageUpdateSerializerV1,
    UserPasswordChangeSerializerV1, UserPasswordForgotSerializerV1,
    UserActivationResendSerializerV1
)
