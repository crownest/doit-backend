# Third-Party
from rest_framework import serializers

# Django
from django.db import models

# Local Django
from users.models import User

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
        fields = ('id', 'first_name', 'last_name', 'email', 'is_active', 'is_superuser')


class UserDetailSerializerV1(UserDetailSerializer):
    class Meta:
        model = User
        fields = ('id',  'first_name', 'last_name', 'email', 'is_active', 'is_superuser')
