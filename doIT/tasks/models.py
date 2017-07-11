from django.db import models
from django.utils import timezone

class Task(models.Model):
        title = models.CharField(max_length=1000, blank=True,
                                 verbose_name="Reminding")

        class Meta:
            ordering = ['title']

        def __str__(self):
            return self.title


class Reminder(models.Model):
        task = models.ForeignKey(Task, verbose_name="Task")
        creation_date = models.DateTimeField(default=timezone.now,
                                             verbose_name="Time")

        def __str__(self):
            return u'%s, %s,' % (self.task, self.creation_date)

        class Meta:
            ordering = ['creation_date']
