# Third-Party
from rest_framework import serializers

# Django
from django.db import models

# Local Django
from tasks.models import Task, Reminder


class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderListSerializerV1(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderDetailSerializerV1(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderCreateSerializerV1(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('task', 'date')


class ReminderUpdateSerializerV1(ReminderSerializer):

    class Meta:
        model = Reminder
        fields = ('date',)


class TaskSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskListSerializerV1(TaskSerializer):

    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskDetailSerializerV1(TaskSerializer):
    reminders = ReminderDetailSerializerV1(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskCreateSerializerV1(TaskSerializer):
    reminders = ReminderCreateSerializerV1(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('title', 'description', 'reminders')


class TaskUpdateSerializerV1(TaskSerializer):

    class Meta:
        model = Task
        fields = ('title', 'description')
