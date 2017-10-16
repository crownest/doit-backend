# Local Django
from .base_serializers import (
    ReminderListSerializer, ReminderCreateSerializer,
    ReminderRetrieveSerializer, ReminderUpdateSerializer,
    TaskListSerializer, TaskCreateSerializer,
    TaskRetrieveSerializer, TaskUpdateSerializer
)


class ReminderListSerializerV1(ReminderListSerializer):
    pass


class ReminderCreateSerializerV1(ReminderCreateSerializer):
    pass


class ReminderRetrieveSerializerV1(ReminderRetrieveSerializer):
    pass


class ReminderUpdateSerializerV1(ReminderUpdateSerializer):
    pass


class TaskListSerializerV1(TaskListSerializer):
    pass


class TaskCreateSerializerV1(TaskCreateSerializer):
    reminders = ReminderCreateSerializerV1(many=True, read_only=True)


class TaskRetrieveSerializerV1(TaskRetrieveSerializer):
    reminders = ReminderRetrieveSerializerV1(many=True, read_only=True)


class TaskUpdateSerializerV1(TaskUpdateSerializer):
    pass
