# Third-Party
from rest_framework import serializers
from easy_thumbnails.files import get_thumbnailer
from django.utils.translation import ugettext_lazy as _

# Django
from django.conf import settings
from django.contrib.auth import password_validation

# Local Django
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    image_128x128 = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'image', 'image_128x128', 'is_active', 'is_verified'
        )

    def get_image(self, obj):
        if obj.image:
            return settings.DOMAIN_BACKEND + obj.image.url
        else:
            return settings.DOMAIN_BACKEND + '/static/img/users/default-user-image.256x256.png'

    def get_image_128x128(self, obj):
        if obj.image:
            try:
                context = {'size': (128, 128)}
                return settings.DOMAIN_BACKEND + get_thumbnailer(obj.image).get_thumbnail(context).url
            except:
                return None
        else:
            return settings.DOMAIN_BACKEND + '/static/img/users/default-user-image.128x128.png'

class UserListSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserRetrieveSerializer(UserSerializer):
    pass


class UserCreateSerializer(UserSerializer):
    confirm_password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        if value != self.initial_data.get('confirm_password', None):
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

        return value


class UserUpdateSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')


class UserImageUpdateSerializer(UserSerializer):
    image = serializers.ImageField()

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
        if value != self.initial_data['new_password']:
            raise serializers.ValidationError(
                "The two password fields didn't match."
            )

        password_validation.validate_password(value)

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
