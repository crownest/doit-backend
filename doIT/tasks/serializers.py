from django.db import models
from rest_framework import serializers
from tasks.models import Task,Reminder

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('user', 'title', 'description')

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = ('task', 'date')
