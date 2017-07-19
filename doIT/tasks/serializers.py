# Third-Party
from rest_framework import serializers

# Django
from django.db import models

# Local Django
from tasks.models import Task, Reminder


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskListSerializerV1(TaskListSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title')


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description')


class TaskDetailSerializerV1(TaskDetailSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description')


class ReminderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderListSerializerV1(ReminderListSerializer):
    task = TaskListSerializerV1()
    
    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')


class ReminderDetailSerializerV1(ReminderDetailSerializer):
    task = TaskDetailSerializerV1()
    
    class Meta:
        model = Reminder
        fields = ('id', 'task', 'date')