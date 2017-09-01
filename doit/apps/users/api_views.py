# Third-Party
from rest_framework import viewsets

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

# Local Django
from users.models import User, ActivationKey
from doit.modules import ActivationKeyModule, MailModule
from users.serializers import (
    UserSerializer,  UserListSerializerV1, UserCreateSerializerV1,
    UserDetailSerializerV1
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return UserListSerializerV1
            elif self.action == 'retrieve':
                return UserDetailSerializerV1
            elif self.action == 'create':
                return UserCreateSerializerV1

        return UserSerializer

    def get_permissions(self):
        permissions = super(UserViewSet, self).get_permissions()

        if self.action == 'create':
            return []

        return permissions

    def perform_create(self, serializer):
        # Create User
        user = serializer.save()
        user.set_password(serializer.validated_data.get('password', ''))
        user.save()

        # Create Activation Key
        activation_key = ActivationKeyModule.create_key(user=user)
        activation_url = settings.DOMAIN + reverse('activation', kwargs={
            'key': activation_key.key
        })

        # Send Activation Mail
        MailModule.send_activation_mail(activation_key)

        return user
