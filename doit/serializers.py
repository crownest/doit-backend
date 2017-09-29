# Django
from django.utils.translation import ugettext_lazy as _

# Third-Party
from rest_framework import serializers
from djoser.serializers import LoginSerializer


class LoginSerializer(LoginSerializer):
    extra_error_messages = {
            _('message'):'Your login information could not be verified'
    }

    def validate(self, attrs):
        super(LoginSerializer, self).validate(attrs)

        if not self.user.is_verify:
            raise serializers.ValidationError(
                self.extra_error_messages['message']
            )

        return attrs
