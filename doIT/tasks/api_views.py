# Third-Party
from rest_framework import viewsets

# Local Django
from .models import Task, Reminder
from .serializers import TaskListSerializer, ReminderListSerializer
from .serializers import TaskDetailSerializer, ReminderDetailSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskListSerializer
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        if self.action == 'retrieve':
            return TaskDetailSerializer
    
        return TaskListSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ReminderListSerializer
        if self.action == 'retrieve':
            return ReminderDetailSerializer
    
        return ReminderListSerializer

