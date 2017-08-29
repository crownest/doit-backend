# Standard Library
import random
import string

# Django
from django.utils.crypto import get_random_string

# Local Django
from users.models import ActivationKey


class ActivationKeyModule(object):

    @staticmethod
    def create_key(user, length=50):
        created = False

        while created==False:
            key = get_random_string(length=length)
            activation_key, created = ActivationKey.objects.get_or_create(
                user=user, key=key
            )

        return activation_key

    @staticmethod
    def get_key(key):
        try:
            activation_key = ActivationKey.objects.get(key=key, is_used=False)
        except ActivationKey.DoesNotExist:
            activation_key = None

        return activation_key