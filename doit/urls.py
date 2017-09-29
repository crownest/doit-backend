# Django
from django.contrib import admin
from django.conf.urls import url, include
from users import views

# Local Django
from doit.api_views import LoginView
from doit.views import DocumentationView, ActivationView


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Documentation
    url(r'^docs/$', DocumentationView.as_view(), name='docs'),
    url(r'^docs/(?P<path>.*)$', DocumentationView.as_view(), name='docs'),

    # Api
    url(r'^api/', include('doit.api_urls')),

    # Token
    url(r'^api-auth/login', LoginView.as_view(), name='login'),
    url(r'^api-auth/', include('djoser.urls.authtoken')),

    # Activation
    url(r'^activation/(?P<key>\w+)/$', ActivationView.as_view(), name='activation'),
]
#abi bir sn müsadenle
