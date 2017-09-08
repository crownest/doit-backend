# Standard Library
import random

# Django
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string

# Local Django
from users.models import ActivationKey
from doit.tasks import send_mail_task


class ActivationKeyModule(object):

    @staticmethod
    def create_key(user, length=50):
        created = False

        while created == False:
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


class MailModule(object):

    @staticmethod
    def send_activation_mail(activation_key):
        template_context = {
            'domain': settings.DOMAIN,
            'full_name': activation_key.user.get_full_name(),
            'activation_url': settings.DOMAIN + reverse(
                'activation', args=[activation_key.key]
            )
        }
        context = {
            'subject': 'Activate Your Account',
            'message': (
                "Doit\n"
                "Hello, {full_name}\n"
                "Activate Your Account = {activation_url}\n").format(
                    full_name=template_context.get('full_name', ''),
                    activation_url=template_context.get('activation_url', '')
                ),
            'html_message': render_to_string(
                'mail/activation-mail.html', template_context
            ),
            'from_email': settings.DEFAULT_FROM_EMAIL,
            'recipient_list': [activation_key.user.email]
        }

        send_mail_task.delay(context, 'activation')
