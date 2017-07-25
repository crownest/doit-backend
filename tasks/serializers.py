# Third-Party
from rest_framework import serializers

# Django
from django.db import models

# Local Django
from tasks.models import Task, Reminder


class ReminderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'date')


class ReminderListSerializerV1(ReminderListSerializer):

    class Meta:
        model = Reminder
        fields = ('id', 'date')


class ReminderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'date')


class ReminderDetailSerializerV1(ReminderDetailSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'date')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskListSerializerV1(TaskListSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskDetailSerializer(serializers.ModelSerializer):
    reminders = ReminderDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskDetailSerializerV1(TaskDetailSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')


class TaskCreateSerializerV1(TaskCreateSerializer):
    reminders = ReminderListSerializerV1(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'reminders')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
