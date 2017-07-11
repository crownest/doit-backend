from django.db import models
from datetime import datetime

class Reminders(models.Model):
	task = models.ForeignKey(Tasks,verbose_name="Görev")
	time = datetime.datetime.now().strftime('%H:%M:%S')
	date = datetime.now()
