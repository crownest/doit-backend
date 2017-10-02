# Third-Party
from rest_framework import serializers

# Django
from django.db import models

# Local Django
from tasks.models import Task, Reminder


# Reminder Base

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderListSerializer(ReminderSerializer):
    pass


class ReminderDetailSerializer(ReminderSerializer):
    pass


class ReminderCreateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('task', 'date')


class ReminderUpdateSerializer(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('date',)


# Reminder V1

class ReminderListSerializerV1(ReminderListSerializer):
    pass


class ReminderDetailSerializerV1(ReminderDetailSerializer):
    pass


class ReminderCreateSerializerV1(ReminderCreateSerializer):
    pass


class ReminderUpdateSerializerV1(ReminderUpdateSerializer):
    pass


# Task Base

class TaskSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskListSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskDetailSerializer(TaskSerializer):
    reminders = ReminderDetailSerializer(many=True, read_only=True)


class TaskCreateSerializer(TaskSerializer):
    reminders = ReminderCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'reminders')


class TaskUpdateSerializer(TaskSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description')


# Task V1

class TaskListSerializerV1(TaskListSerializer):
    pass


class TaskDetailSerializerV1(TaskDetailSerializer):
    reminders = ReminderDetailSerializerV1(many=True, read_only=True)


class TaskCreateSerializerV1(TaskCreateSerializer):
    reminders = ReminderCreateSerializerV1(many=True, read_only=True)


class TaskUpdateSerializerV1(TaskUpdateSerializer):
    pass
