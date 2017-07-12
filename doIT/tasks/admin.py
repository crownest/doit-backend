from django.contrib import admin
from tasks.models import Reminder, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('title', 'description')
    list_display = ('title', 'get_task_title',)
    list_filter = ('title',)
    search_fields = ('description', 'title',)

    def get_task_title(self, obj):
        return obj.title
    get_task_title.admin_order_field = 'title'
    get_task_title.short_description = 'Tasks'

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    fields = ('task', 'date',)
    list_display = ('get_taskr_title', 'date', )
    list_filter = ('date',)
    search_fields = ('task__title',)

    def get_taskr_title(self, obj):
        return obj.task.title
    get_taskr_title.admin_order_field = 'task'
    get_taskr_title.short_description = 'Task'
