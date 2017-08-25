 # Third-Party
from rest_framework import serializers

# Local Django
from users.models import User, ActivationKey
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.conf import settings


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserListSerializerV1(UserListSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name',
            'email', 'is_active', 'is_superuser'
        )


class UserDetailSerializerV1(UserDetailSerializer):
    class Meta:
        model = User
        fields = (
            'id',  'first_name', 'last_name',
            'email', 'is_active', 'is_superuser'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
             'email', 'first_name', 'last_name', 'password'
         )


class UserCreateSerializerV1(UserCreateSerializer):
    class Meta:
        model = User
        fields = (
             'email', 'first_name', 'last_name', 'password'
         )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        key = ActivationKey.objects.create(user=user)
        verify_url = settings.DOMAIN + reverse('verify', kwargs={'key': key})
        send_mail(
            'Doit e-mail activation',
            verify_url,
            'doit@unicrow.com',
            [user.email],
            fail_silently=False)
        return user
