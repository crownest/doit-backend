# Third-Party
from rest_framework import serializers
from djoser.serializers import LoginSerializer as _LoginSerializer

# Django
from django.utils.translation import ugettext_lazy as _

# Local Django
from core.models import Contact


class LoginSerializer(_LoginSerializer):
    extra_error_messages = {
        'unverified_account': _('User account is unverified.')
    }

    def validate(self, attrs):
        super(LoginSerializer, self).validate(attrs)

        self._validate_user_is_verified(self.user)

        return attrs

    def _validate_user_is_verified(self, user):
        if not self.user.is_verified:
            raise serializers.ValidationError(
                self.extra_error_messages['unverified_account']
            )


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'message')


class ContactCreateSerializer(ContactSerializer):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
