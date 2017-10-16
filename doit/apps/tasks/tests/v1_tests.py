# Third-Party
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from .base_tests import ReminderAPITestCase, TaskAPITestCase


class ReminderAPIV1TestCase(ReminderAPITestCase):

    def test_list_reminder(self):
        url = reverse('v1:reminders-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TaskAPIV1TestCase(TaskAPITestCase):

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
