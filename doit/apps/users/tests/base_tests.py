# Third-Party
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

# Django
from django.urls import reverse

# Local Django
from users.models import User
from doit.modules import ActivationKeyModule


class TokenAPITestCase(APITestCase):

    def setUp(self):
        # Create User
        self.email = 'doit@unicrow.com'
        self.first_name = 'Doit'
        self.last_name = 'Apps'
        self.password = 'test'
        self.user = User.objects.create_user(
            email=self.email, password=self.password
        )
        self.user.first_name = self.first_name
        self.user.last_name = self.last_name
        self.user.is_verified = True
        self.user.save()

    def test_login_verified(self):
        dummy_data = {
            'email': self.email,
            'password': self.password
        }
        url = reverse('login')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_unverified(self):
        dummy_data = {
            'email': self.email,
            'password': self.password
        }
        self.user.is_verified = False
        self.user.save()
        url = reverse('login')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UserAPITestCase(APITestCase):
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
