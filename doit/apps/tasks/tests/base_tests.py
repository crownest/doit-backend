# Standart Library
import datetime

# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from tasks.models import Reminder, Task


class ReminderAPITestCase(APITestCase):

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user('doit@unicrow.com', '123456test')
        self.user.first_name = 'Doit'
        self.user.last_name = 'Apps'
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Token Authentication
        self.api_authentication()

        # Create Task
        self.task = Task.objects.create(
            title='Sport', description='Basketball', user=self.user
        )

        # Create Dummy Data
        self.date = datetime.datetime.utcnow() + datetime.timedelta(minutes=5)
        self.date_str = self.date.strftime('%Y-%m-%dT%H:%M:%S')
        self.dummy_data = {
            'task': self.task.id,
            'date': self.date_str
        }

        # Create Reminder
        self.reminder = Reminder.objects.create(
            task=self.task,
            date=datetime.datetime.strptime(self.date_str, '%Y-%m-%dT%H:%M:%S')
        )

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


class TaskAPITestCase(APITestCase):
    dummy_data = {
        'title': 'Sport',
        'description': 'Basketball'
    }

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user('doit@unicrow.com', '123456test')
        self.user.first_name = 'Doit'
        self.user.last_name = 'Apps'
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Token Authentication
        self.api_authentication()

        # Create Task
        self.task = Task.objects.create(user=self.user, **self.dummy_data)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
