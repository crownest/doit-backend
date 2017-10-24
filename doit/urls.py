# Django
from django.contrib import admin
from django.conf.urls import url, include
from users import views

# Local Django
from core.api_views import LoginView
from doit.views import DocumentationView, ActivationView, ResetPasswordView


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Documentation
    url(r'^docs/$', DocumentationView.as_view(), name='docs'),
    url(r'^docs/(?P<path>.*)$', DocumentationView.as_view(), name='docs'),

    # Api
    url(r'^', include('doit.api_urls')),

    # Token
    url(r'^auth/login', LoginView.as_view(), name='login'),
    url(r'^auth/', include('djoser.urls.authtoken')),

    # Activation and Password Operations
    url(r'^activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
    url(r'^reset-password/(?P<key>\w+)/$', ResetPasswordView.as_view(), name='reset-password')
]
