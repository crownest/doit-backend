# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase

# Django
from django.urls import reverse

# Local Django
from users.models import User


class UserAPIV1TestCase(APITestCase):
    dummy_data = {
        'email': 'doit@unicrow.com',
        'first_name': 'Doit',
        'last_name': 'Apps',
        'password': 'test'
    }

    def test_create_user(self):
        url = reverse('v1:users-list')

        # Create User
        response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(201, response.status_code)

        # Check User Info
        user = User.objects.get(email=self.dummy_data.get('email', None))
        self.assertEqual(user.email, self.dummy_data.get('email', None))
        self.assertEqual(user.first_name, self.dummy_data.get('first_name', None))
        self.assertEqual(user.last_name, self.dummy_data.get('last_name', None))
        self.assertTrue(user.check_password(self.dummy_data.get('password', None)))
        self.assertFalse(user.is_verified)
