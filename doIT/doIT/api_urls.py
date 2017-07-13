# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from tasks.api_views import  TaskViewSet, ReminderViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    url(r'v1/', include(router.urls))
]
