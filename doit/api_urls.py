# Django
from django.conf.urls import url, include

# Third-Party
from rest_framework import routers

# Local Django
from users.api_views import UserViewSetV1
from tasks.api_views import TaskViewSetV1, ReminderViewSetV1


router_V1 = routers.DefaultRouter()

LIST_V1 = [
    (r'users', UserViewSetV1, 'users-v1'),
    (r'tasks', TaskViewSetV1, 'tasks-v1'),
    (r'reminders', ReminderViewSetV1, 'reminders-v1')
]

for router in LIST_V1:
    router_V1.register(router[0], router[1], base_name=router[2])


urlpatterns = [
    url(r'v1/', include(router_V1.urls, namespace='v1')),
]
