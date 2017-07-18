# Django
from django.contrib import admin
from django.conf.urls import url, include
#Third-Party
import rest_framework_jwt.views
import djoser.views


urlpatterns = [
    # Admin
    url(r'^admin/', admin.site.urls),

    # Api
    url(r'^api/', include('doIT.api_urls')),

    #Djoser
    url(r'^api-auth/', include('djoser.urls.authtoken')),

]
