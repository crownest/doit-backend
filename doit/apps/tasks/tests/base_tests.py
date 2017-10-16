# Third-Party
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Local Django
from users.models import User
from tasks.models import Task


class TaskAPITestCase(APITestCase):
    dummy_data = {
        'title': 'Sport',
        'description': 'Basketball'
    }

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user('doit@unicrow.com', 'test')
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
