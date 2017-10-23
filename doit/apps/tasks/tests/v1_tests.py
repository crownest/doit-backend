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

    def test_create_reminder(self):
        url = reverse('v1:reminders-list')

        response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.dummy_data)

    def test_retrieve_reminder(self):
        url = reverse('v1:reminders-detail', kwargs={'pk': self.reminder.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.reminder.id)
        self.assertEqual(response.data.get('task', None), self.reminder.task.id)
        self.assertEqual(
            response.data.get('date', None),
            self.reminder.date.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

    def test_update_reminder(self):
        dummy_data = {
            'date': '2017-12-19T15:00:00Z'
        }
        url = reverse('v1:reminders-detail', kwargs={'pk': self.reminder.id})

        response = self.client.put(url, dummy_data, format='json')
        self.reminder.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dummy_data)
        self.assertEqual(
            response.data.get('date', None),
            self.reminder.date.strftime('%Y-%m-%dT%H:%M:%SZ')
        )

    def test_delete_reminder(self):
        url = reverse('v1:reminders-detail', kwargs={'pk': self.reminder.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


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
        self.assertEqual(response.data.get('id', None), self.task.id)
        self.assertEqual(response.data.get('title', None), self.task.title)
        self.assertEqual(response.data.get('description', None), self.task.description)

    def test_update_task(self):
        dummy_data = {
            'title': 'Drink Tea',
            'description': 'Chai Masala'
        }
        url = reverse('v1:tasks-detail', kwargs={'pk': self.task.id})

        response = self.client.put(url, dummy_data, format='json')
        self.task.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dummy_data)
        self.assertEqual(response.data.get('title', None), self.task.title)
        self.assertEqual(response.data.get('description', None), self.task.description)

    def test_delete_task(self):
        url = reverse('v1:tasks-detail', kwargs={'pk': self.task.id})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
