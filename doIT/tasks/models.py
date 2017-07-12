from django.db import models
from django.utils import timezone


class Task(models.Model):
        title = models.CharField(
            verbose_name="Reminding", max_length=1000, blank=True
        )

        class Meta:
            ordering = ('title',)

        def __str__(self):
            return '{title}'.format(title=self.title)


class Reminder(models.Model):
        task = models.ForeignKey(
            verbose_name='Task', to='tasks.Task', related_name='reminders'
        )
        date = models.DateTimeField(verbose_name='Time')

        def __str__(self):
            return '{task} {date}'.format(task=self.task.__str__(), date=self.date)

        class Meta:
            ordering = ('date',)
