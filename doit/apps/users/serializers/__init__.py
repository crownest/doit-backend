# Local Django
from .base_serializers import (
    UserSerializer, UserListSerializer, UserCreateSerializer,
    UserRetrieveSerializer, UserUpdateSerializer,
    UserPasswordChangeSerializer, UserPasswordForgotSerializer,
    UserActivationResendSerializer
)
from .v1_serializers import (
    UserListSerializerV1, UserCreateSerializerV1,
    UserRetrieveSerializerV1, UserUpdateSerializerV1,
    UserPasswordChangeSerializerV1, UserPasswordForgotSerializerV1,
    UserActivationResendSerializerV1
)
