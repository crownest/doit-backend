# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from tasks.api_views import  TaskViewSet

router = routers.DefaultRouter()


router.register(r'tasks', TaskViewSet)


urlpatterns = [
    url(r'v1/', include(router.urls))
]
