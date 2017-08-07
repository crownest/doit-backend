# Third-Party
from rest_framework import viewsets

# Local Django
from users.models import User
from users.serializers import (
    UserListSerializer, UserListSerializerV1,
    UserDetailSerializer, UserDetailSerializerV1
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.user(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return UserListSerializerV1
            elif self.action == 'retrieve':
                return UserDetailSerializerV1

        return UserListSerializer
