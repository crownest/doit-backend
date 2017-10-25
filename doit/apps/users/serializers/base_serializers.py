# Third-Party
from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings

# Local Django
from users.models import User
from django.contrib.auth import password_validation


class UserSerializer(serializers.ModelSerializer):
    image_200x200 = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'image', 'image_200x200', 'is_active', 'is_verified'
        )

    def get_image_200x200(self, obj):
        try:
            context = {'size': (200, 200)}
            return settings.DOMAIN + get_thumbnailer(obj.image).get_thumbnail(context).url
        except:
            return None


class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserRetrieveSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class UserImageUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('image',)
        extra_kwargs = {'image': {'required': True}}


class UserPasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_new_password = serializers.CharField()

    class Meta:
        fields = ('old_password', 'new_password', 'confirm_new_password')

    def validate_confirm_new_password(self, value):
        if self.initial_data['new_password'] != self.initial_data['confirm_new_password']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(
            self.initial_data['confirm_new_password']
        )

        return value

    def validate_old_password(self, value):
        user = self.context['user']

        if not user.check_password(value):
            raise serializers.ValidationError(_(
                'Your old password was entered incorrectly. '
                'Please enter it again.'
            ))

        return value


class UserPasswordForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def validate_email(self, value):
        self.user = None
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(_('User not found!'))

        return value


class UserActivationResendSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ('email',)

    def validate_email(self, value):
        self.user = None
        try:
            self.user = User.objects.get(email=value)

            if self.user.is_verified:
                raise serializers.ValidationError(_('User already verifed!'))
        except User.DoesNotExist:
            raise serializers.ValidationError(_('User not found!'))

        return value
