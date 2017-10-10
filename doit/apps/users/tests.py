# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Django
from django.urls import reverse

# Local Django
from users.models import User
from doit.modules import ActivationKeyModule


class UserAPIV1TestCase(APITestCase):
    dummy_data = {
        'email': 'doit@unicrow.com',
        'first_name': 'Doit',
        'last_name': 'Apps',
        'password': 'test'
    }

    def setUp(self):
        # Create User and Token
        self.user = User.objects.create_user(
            email=self.dummy_data.get('email', None),
            password=self.dummy_data.get('password', None)
        )
        self.user.first_name = self.dummy_data.get('first_name', None)
        self.user.last_name = self.dummy_data.get('last_name', None)
        self.user.save()
        self.token = Token.objects.create(user=self.user)

        # Create Activation Key
        self.activation_key = ActivationKeyModule.create_key(user=self.user)

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_list_user(self):
          url = reverse('v1:users-list')
          self.api_authentication()

          response = self.client.get(url)
          self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        dummy_data = {
            'email': 'crownest@unicrow.com',
            'first_name': 'Crownest',
            'last_name': 'Apps',
            'password': 'test'
        }
        url = reverse('v1:users-list')

        # Create User
        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check User Info
        user = User.objects.get(email=dummy_data.get('email', None))
        self.assertEqual(user.email, dummy_data.get('email', None))
        self.assertEqual(user.first_name, dummy_data.get('first_name', None))
        self.assertEqual(user.last_name, dummy_data.get('last_name', None))
        self.assertTrue(user.check_password(dummy_data.get('password', None)))
        self.assertFalse(user.is_verified)

    def test_activation_user(self):
        self.assertFalse(self.user.is_verified)
        self.assertFalse(self.activation_key.is_used)

        url = reverse('activation', kwargs={'key': self.activation_key.key})
        response = self.client.get(url)
        self.user.refresh_from_db()
        self.activation_key.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.user.is_verified)
        self.assertTrue(self.activation_key.is_used)

    def test_update_user(self):
        dummy_data = {
            'email': 'example@unicrow.com',
            'first_name': 'Example',
            'last_name': 'Apps'
        }
        url = reverse('v1:users-detail', kwargs={'pk': self.user.id})
        self.api_authentication()

        response = self.client.put(url, dummy_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dummy_data)
        self.assertEqual(self.user.email, dummy_data.get('email', None))
        self.assertEqual(self.user.first_name, dummy_data.get('first_name', None))
        self.assertEqual(self.user.last_name, dummy_data.get('last_name', None))
