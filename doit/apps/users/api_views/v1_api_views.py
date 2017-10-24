# Local Django
from .base_api_views import UserViewSet
from users.serializers import (
    UserSerializer, UserListSerializerV1, UserCreateSerializerV1,
    UserRetrieveSerializerV1, UserUpdateSerializerV1,
    UserPasswordChangeSerializerV1, UserPasswordForgotSerializerV1
)


class UserViewSetV1(UserViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializerV1
        elif self.action == 'create':
            return UserCreateSerializerV1
        elif self.action == 'retrieve':
            return UserRetrieveSerializerV1
        elif self.action == 'update':
            return UserUpdateSerializerV1
        else:
            return UserSerializer

    def get_route_serializer_class(self):
        if self.action == 'change_password':
            return UserPasswordChangeSerializerV1
        elif self.action == 'forgot_password':
            return UserPasswordForgotSerializerV1
        else:
            return UserSerializer
