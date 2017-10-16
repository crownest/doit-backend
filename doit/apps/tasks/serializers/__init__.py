# Local Django
from .base_serializers import (
    ReminderSerializer, ReminderListSerializer, ReminderCreateSerializer,
    ReminderRetrieveSerializer, ReminderUpdateSerializer,
    TaskSerializer, TaskListSerializer, TaskCreateSerializer,
    TaskRetrieveSerializer, TaskUpdateSerializer
)
from .v1_serializers import (
    ReminderListSerializerV1, ReminderCreateSerializerV1,
    ReminderRetrieveSerializerV1, ReminderUpdateSerializerV1,
    TaskListSerializerV1, TaskCreateSerializerV1,
    TaskRetrieveSerializerV1, TaskUpdateSerializerV1
)
