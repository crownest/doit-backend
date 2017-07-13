from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', views.TaskList.as_view()),
    url(r'^reminders/', views.ReminderList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
