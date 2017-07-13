# Third-Party
from rest_framework import viewsets

# Local Django
from tasks.models import Task, Reminder
from tasks.serializers import TaskListSerializer, ReminderListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()


class ReminderViewSet(viewsets.ModelViewSet):
    serializer_class = ReminderListSerializer
    queryset = Reminder.objects.all()
