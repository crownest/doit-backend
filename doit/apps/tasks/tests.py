# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Django
from django.urls import reverse

# Local Django
from users.models import User
from tasks.models import Task


class TaskAPIV1TestCase(APITestCase):
    task_dummy_data = {
        'title': 'Sport',
        'description': 'Basketball'
    }

    def setUp(self):
        self.email = "doit@unicrow.com"
        self.password = "test"
        self.user = User.objects.create_user(self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_retrieve_task(self):
        task = Task.objects.create(user=self.user, **self.task_dummy_data)
        url = reverse('v1:tasks-detail', kwargs={'pk': task.id})

        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
