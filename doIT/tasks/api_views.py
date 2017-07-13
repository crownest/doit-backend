# Third-Party
from rest_framework import viewsets

# Local Django
from tasks.models import Task, Reminder
from tasks.serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
