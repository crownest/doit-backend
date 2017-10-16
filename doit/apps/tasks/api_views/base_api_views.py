# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from tasks.models import Task, Reminder
from tasks.serializers import (
    ReminderSerializer, ReminderListSerializer, ReminderCreateSerializer,
    ReminderRetrieveSerializer, ReminderUpdateSerializer,
    TaskSerializer, TaskListSerializer, TaskCreateSerializer,
    TaskRetrieveSerializer, TaskUpdateSerializer
)


class ReminderViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Reminder.objects.all()

    def get_queryset(self):
        return self.queryset.filter(task__user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ReminderListSerializer
        elif self.action == 'create':
            return ReminderCreateSerializer
        elif self.action == 'retrieve':
            return ReminderRetrieveSerializer
        elif self.action == 'update':
            return ReminderUpdateSerializer
        else:
            return ReminderSerializer


class TaskViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        elif self.action == 'create':
            return TaskCreateSerializer
        elif self.action == 'retrieve':
            return TaskRetrieveSerializer
        elif self.action == 'update':
            return TaskUpdateSerializer
        else:
            return TaskSerializer

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)

        reminders_data = self.request.data.get('reminders', [])
        for reminder_data in reminders_data:
            Reminder.objects.create(task=task, **reminder_data)
