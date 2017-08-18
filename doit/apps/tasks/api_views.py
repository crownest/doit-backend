# Third-Party
from rest_framework import viewsets

# Local Django
from tasks.models import Task, Reminder
from tasks.serializers import (
    TaskListSerializer, TaskListSerializerV1,
    TaskDetailSerializerV1, TaskCreateSerializerV1,
    ReminderListSerializer, ReminderListSerializerV1, ReminderDetailSerializerV1
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return TaskListSerializerV1
            elif self.action == 'retrieve':
                return TaskDetailSerializerV1
            elif self.action == 'create':
                return TaskCreateSerializerV1

        return TaskListSerializer

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)

        reminders_data = self.request.data.get('reminders', [])
        for reminder_data in reminders_data:
            Reminder.objects.create(task=task, **reminder_data)


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()

    def get_queryset(self):
        return self.queryset.filter(task__user=self.request.user)

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return ReminderListSerializerV1
            elif self.action == 'retrieve':
                return ReminderDetailSerializerV1

        return ReminderListSerializer
