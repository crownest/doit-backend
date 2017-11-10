# Standart Library
import io

# Third-Party
from PIL import Image
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from users.models import User
from .base_tests import UserAPITestCase


class UserAPIV1TestCase(UserAPITestCase):

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
            'password': '123456test',
            'confirm_password': '123456test'
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

    def test_retrieve_user(self):
        url = reverse('v1:users-detail', kwargs={'pk': self.user.id})
        self.api_authentication()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id', None), self.user.id)
        self.assertEqual(response.data.get('email', None), self.user.email)
        self.assertEqual(response.data.get('first_name', None), self.user.first_name)
        self.assertEqual(response.data.get('last_name', None), self.user.last_name)
        self.assertEqual(response.data.get('is_active', None), self.user.is_active)
        self.assertEqual(response.data.get('is_verified', None), self.user.is_verified)

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
        self.assertEqual(response.data.get('email', None), self.user.email)
        self.assertEqual(response.data.get('first_name', None), self.user.first_name)
        self.assertEqual(response.data.get('last_name', None), self.user.last_name)

    def test_update_image_user(self):
        # Create image
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)

        dummy_data = {
            'image': file
        }
        url = reverse('v1:users-update-image', kwargs={'pk': self.user.id})
        self.api_authentication()

        response = self.client.post(url, dummy_data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_image_user(self):
        url = reverse('v1:users-delete-image', kwargs={'pk': self.user.id})
        self.api_authentication()

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_change_password_user(self):
        dummy_data = {
            'old_password': '123456test',
            'new_password': '123456doit',
            'confirm_new_password': '123456doit'
        }
        url = reverse('v1:users-change-password', kwargs={'pk': self.user.id})
        self.api_authentication()

        response = self.client.post(url, dummy_data, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            self.user.check_password(dummy_data.get('new_password', None))
        )

    def test_forgot_password_user(self):
        dummy_data = {
            'email': self.user.email
        }
        url = reverse('v1:users-forgot-password')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_resend_activation_user(self):
        dummy_data = {
            'email': self.user.email
        }
        url = reverse('v1:users-resend-activation')

        response = self.client.post(url, dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
