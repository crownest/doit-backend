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

    def test_list_task(self):
        url = reverse('v1:tasks-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = reverse('v1:tasks-list')

        response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data.get('title', None),
            self.dummy_data.get('title', None)
        )
        self.assertEqual(
            response.data.get('description', None),
            self.dummy_data.get('description', None)
        )

    def test_retrieve_task(self):
        url = reverse('v1:tasks-detail', kwargs={'pk': self.task.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data.get('title', None),
            self.dummy_data.get('title', None)
        )
        self.assertEqual(
            response.data.get('description', None),
            self.dummy_data.get('description', None)
        )
