# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

#Local Django
from users.managers import UserManager
from random import choice
from string import hexdigits


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('Email'), max_length=255, unique=True
    )
    first_name = models.CharField(verbose_name=_('First Name'), max_length=50)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=50)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Staff'), default=False)
    is_verify = models.BooleanField(verbose_name=_('Verify'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{first_name} {last_name}'.format(
            first_name=self.first_name, last_name=self.last_name
        )

    def get_short_name(self):
        return '{first_name}'.format(first_name=self.first_name)


def activation_key():
    while True :
        key = (''.join(choice(hexdigits) for i in range(50)))
        if ActivationKey.objects.filter(key=key).count() == 0:
            return key

class ActivationKey(models.Model):
    user = models.ForeignKey(verbose_name=_('User'), to='users.User',
                             related_name='activationkey')
    is_used = models.BooleanField(verbose_name=_('Used'), default=False)
    key = models.CharField(verbose_name=_('Key'), max_length=50,
                           unique=True)

    class Meta:
        verbose_name = _('ActivationKey')
        verbose_name_plural = _('ActivationKey')

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.pk:
            self.key = activation_key()
            super(ActivationKey, self).save(*args, **kwargs)
