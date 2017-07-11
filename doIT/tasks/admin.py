from django.contrib import admin
from tasks.models import Reminder, Task

admin.site.register(Task)
admin.site.register(Reminder)
