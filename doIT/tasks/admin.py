from django.contrib import admin
from tasks.models import Reminder, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'description')
    list_filter = ('title',)
    search_fields = ('description', 'title',)

    def get_task_title(self, obj):
        return obj.title

    def get_desc(self, obj):
        return obj.description
    get_desc.admin_order_field = 'description'


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    fields = ('task', 'date',)
    list_display = ('get_taskr_title', 'date')
    list_filter = ('date', 'task__title')
    search_fields = ('task__title',)

    def get_taskr_title(self, obj):
        return obj.task.title
    get_taskr_title.short_description = 'Task'
