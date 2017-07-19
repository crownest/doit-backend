# Third-Party
from rest_framework import viewsets

# Local Django
from .models import User
from .serializers import (
    UserListSerializer, UserListSerializerV1,
    UserDetailSerializer, UserDetailSerializerV1 
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_queryset(self):
        user = self.request.user

        if not user.is_superuser:
            return self.queryset.filter(id=user.id)
        else:
            return self.queryset
    
    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return UserListSerializerV1
            elif self.action == 'retrieve':
                return UserDetailSerializerV1
        
        return UserListSerializer

