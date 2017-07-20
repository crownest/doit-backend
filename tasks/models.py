from django.db import models
from django.utils import timezone
from datetime import datetime


class Task(models.Model):
        title = models.CharField(
            verbose_name='Title', max_length=1000, blank=True
        )
        description = models.TextField(
            verbose_name='Description', max_length=10000, null=True
        )
        user = models.ForeignKey(
            verbose_name='User', to='users.User', related_name='users'
        )

        class Meta:
            ordering = ('id',)

        def __str__(self):
            return '{title}'.format(title=self.title)



class Reminder(models.Model):
        task = models.ForeignKey(
            verbose_name='Task', to='tasks.Task', related_name='reminders'
        )
        date = models.DateTimeField(
            verbose_name='Time', blank=True, null=True,
        )

        def __str__(self):
            return '{task}'.format(task=self.task.__str__())

        class Meta:
            ordering = ('date',)