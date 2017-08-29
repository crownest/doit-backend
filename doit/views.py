# Django
from django.conf import settings
from django.contrib import messages
from django.views.static import serve
from django.views.generic import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Local Django
from users.models import ActivationKey
from doit.modules import ActivationKeyModule


class DocumentationView(View):

    def get(self, request, path='index.html', **kwargs):
        return serve(
            request, path, document_root=settings.DOCUMENTATION_ROOT, **kwargs
        )


class ActivationView(TemplateView):
    template_name = 'activation.html'

    def dispatch(self, request, key, *args, **kwargs):
        self.activation(key)

        if request.user.is_authenticated():
            if self.activation_key:
                messages.success(request, self.activation_message)
            else:
                messages.error(request, self.activation_message)

            return redirect('/admin/')

        return super(ActivationView, self).dispatch(request, key, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ActivationView, self).get_context_data(**kwargs)

        context.update({
            'title': 'Activation',
            'activation_key': self.activation_key,
            'activation_message': self.activation_message
        })

        return context

    def activation(self, key):
        self.activation_message = ''
        self.activation_key = ActivationKeyModule.get_key(key)

        if self.activation_key:
            # User verified.
            self.activation_key.user.is_verify = True
            self.activation_key.user.save()

            # Key disabled.
            self.activation_key.is_used = True
            self.activation_key.save()

            self.activation_message = 'Activation is successfully completed.'
        else:
            self.activation_message = 'Incorrect key!'
