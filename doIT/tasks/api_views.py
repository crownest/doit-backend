# Third-Party
from rest_framework import viewsets


# Local Django
from .models import Task, Reminder
from .serializers import (
    TaskListSerializer, ReminderListSerializer,
    TaskListSerializerV1, ReminderListSerializerV1,
    TaskDetailSerializerV1, ReminderDetailSerializerV1
)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        print(self.request.version)
        if self.request.version == 'v1':
            print('Burda1')
            if self.action == 'list':
                print('Burda2')
                return TaskListSerializerV1
            elif self.action == 'retrieve':
                print('Burda3')
                return TaskDetailSerializerV1
        
        return TaskListSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()

    def get_serializer_class(self):
        if self.request.version == 'v1':
            if self.action == 'list':
                return ReminderListSerializerV1
            elif self.action == 'retrieve':
                return ReminderDetailSerializerV1
        
        return ReminderListSerializer

