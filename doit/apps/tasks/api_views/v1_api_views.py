# Local Django
from .base_api_views import ReminderViewSet, TaskViewSet
from tasks.serializers import (
    ReminderSerializer, ReminderListSerializerV1, ReminderCreateSerializerV1,
    ReminderRetrieveSerializerV1, ReminderUpdateSerializerV1,
    TaskSerializer, TaskListSerializerV1, TaskCreateSerializerV1,
    TaskRetrieveSerializerV1, TaskUpdateSerializerV1,
)


class ReminderViewSetV1(ReminderViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return ReminderListSerializerV1
        elif self.action == 'create':
            return ReminderCreateSerializerV1
        elif self.action == 'retrieve':
            return ReminderRetrieveSerializerV1
        elif self.action == 'update':
            return ReminderUpdateSerializerV1
        else:
            return ReminderSerializer


class TaskViewSetV1(TaskViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializerV1
        elif self.action == 'create':
            return TaskCreateSerializerV1
        elif self.action == 'retrieve':
            return TaskRetrieveSerializerV1
        elif self.action == 'update':
            return TaskUpdateSerializerV1
        else:
            return TaskSerializer
