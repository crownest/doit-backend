from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Task, Reminder
from tasks.serializers import TaskSerializer
from tasks.serializers import ReminderSerializer

class TaskList(APIView):

    def get(self,request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


class ReminderList(APIView):

    def get(self,request):
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
