from django.contrib import admin
from tasks.models import Reminder, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ('user', 'title', 'description')
    list_display = ('get_task_title', 'get_desc')
    search_fields = ('title', 'description')

    def get_task_title(self, obj):
        return obj.title
    get_task_title.short_description = "Reminder"

    def get_desc(self, obj):
        return obj.description
    get_desc.short_description = "Description"


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    fields = ('task', 'date',)
    list_display = ('get_task_title', 'get_date')
    list_filter = ('date',)
    search_fields = ('task__title',)

    def get_task_title(self, obj):
        return obj.task.title
    get_task_title.short_description = "Tasks"

    def get_date(self, obj):
        return obj.date
    get_date.short_description = "Date"
