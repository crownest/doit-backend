# Third-Party
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets, mixins, status

# Django
from django.core.mail import send_mail

# Local Django
from users.models import User, ActivationKey
from doit.modules import ActivationKeyModule, MailModule
from users.serializers import (
    UserSerializer,  UserListSerializerV1, UserCreateSerializerV1,
    UserDetailSerializerV1, UserUpdateSerializerV1
)


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
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
            elif self.action == 'update':
                return UserUpdateSerializerV1

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

        # Send Activation Mail
        MailModule.send_activation_mail(activation_key)

        return user

    # Change Password
    @detail_route(methods=['post'], url_path='password/change')
    def change_password(self, request, pk=None):
        user = self.get_object()
        old_password = request.data.get('old_password', None)
        new_password = request.data.get('new_password', None)
        confirm_new_password = request.data.get('confirm_new_password', None)

        content = {
            'messsage': ''
        }

        if user.check_password(old_password):
            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.save()
                content["messsage"] =
                'Your password has been successfully changed'
                return Response(content, status=status.HTTP_200_OK)
            else:
                content["messsage"] =
                'The passwords you entered are not the same'
                return Response(content, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            content["messsage"] =
            'The password you want to change is incorrect'
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
