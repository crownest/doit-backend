# Local Django
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import Http404
from users.models import User, ActivationKey


def verify(request, key):
    try:
        activation_key = ActivationKey.objects.get(key=key)
    except ActivationKey.DoesNotExist:
        activation_key = None

    if activation_key:
        activation_key.user.is_verify = True
        activation_key.user.save()
        return redirect('login')
    else:
        raise Http404("Sorry, Your registration could not be created.")
