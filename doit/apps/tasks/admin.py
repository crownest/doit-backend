# Django
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Local Django
from doit.modules import ReminderModule
from tasks.models import Reminder, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    actions = ['recreate_reminders_celery_task']

    fields = ('user', 'title', 'description')
    
    list_display = ('title', 'user', 'status')
    search_fields = ('title', 'user__email', 'user__first_name', 'user__last_name')

    def recreate_reminders_celery_task(self, request, queryset):
        for task in queryset:
            reminders = task.reminders.all()
            for reminder in reminders:
                ReminderModule.update_celery_task(reminder)
    recreate_reminders_celery_task.short_description = _(
        'Recreate reminders celery task selected Tasks'
    )


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    actions = ['recreate_celery_task']

    fields = ('task', 'date', 'locale_date', 'celery_task_id')
    readonly_fields = ('locale_date', 'celery_task_id')

    list_display = ('task', 'date', 'celery_task_id', '_is_completed')
    list_filter = ('date',)
    search_fields = (
        'task__title', 'task__user__email',
        'task__user__first_name', 'task__user__last_name'
    )

    def recreate_celery_task(self, request, queryset):
        for reminder in queryset:
            ReminderModule.update_celery_task(reminder)
    recreate_celery_task.short_description = _(
        'Recreate celery task selected Reminders'
    )
