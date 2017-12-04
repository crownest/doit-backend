# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):
    title = models.CharField(
        verbose_name=_('Title'), max_length=1000
    )
    description = models.TextField(
        verbose_name=_('Description'), max_length=10000, blank=True
    )
    user = models.ForeignKey(
        verbose_name=_('User'), to='users.User', related_name='tasks'
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = ('Tasks')
        ordering = ('user', '-id')

    def __str__(self):
        return '{title}'.format(title=self.title)


class Reminder(models.Model):
    date = models.DateTimeField(verbose_name=_('Date'))
    celery_task_id = models.CharField(
        verbose_name=_('Celery Task Id'), max_length=254, null=True, blank=True
    )
    task = models.ForeignKey(
        verbose_name=_('Task'), to='tasks.Task', related_name='reminders'
    )

    class Meta:
        verbose_name = _('Reminder')
        verbose_name_plural = _('Reminders')
        ordering = ('task', 'date')

    def __str__(self):
        return '{task} - {date}'.format(
            task=self.task.title, date=self.date
        )
