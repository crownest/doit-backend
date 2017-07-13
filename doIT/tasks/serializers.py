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


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description')


class ReminderListSerializer(serializers.ModelSerializer):
    task = TaskListSerializer()

    class Meta:
        model = Reminder
        fields = ('task','date')

class ReminderDetailSerializer(serializers.ModelSerializer):
    task = TaskDetailSerializer()

    class Meta:
        model = Reminder
        fields = ('task','date')
