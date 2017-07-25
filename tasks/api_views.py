# Third-Party
from rest_framework import viewsets


# Local Django
from .models import Task, Reminder
from .serializers import (TaskListSerializer, TaskListSerializerV1,
    TaskDetailSerializerV1, TaskCreateSerializer, TaskCreateSerializerV1,
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return self.queryset.filter(user=user)
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return TaskListSerializerV1
            elif self.action == 'retrieve':
                return TaskDetailSerializerV1
            elif self.action == 'create':
                return  TaskCreateSerializerV1

        return TaskListSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return self.queryset.filter(task__user=user)
        else:
            return self.queryset

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return ReminderListSerializerV1
            elif self.action == 'retrieve':
                return ReminderDetailSerializerV1

        return ReminderListSerializer
