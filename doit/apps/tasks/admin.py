# Django
from django.contrib import admin

# Local Django
from tasks.models import Reminder, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'description')
    
    list_display = ('title', 'user')
    search_fields = ('title', 'user__email', 'user__first_name', 'user__last_name')


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    fields = ('task', 'date',)

    list_display = ('task', 'date')
    list_filter = ('date',)
    search_fields = (
        'task__title', 'task__user__email',
        'task__user__first_name', 'task__user__last_name'
    )
