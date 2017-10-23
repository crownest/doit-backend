# Third-Party
from rest_framework import status

# Django
from django.urls import reverse

# Local Django
from .base_tests import ContactAPITestCase


class ContactAPIV1TestCase(ContactAPITestCase):

    def test_create_contact(self):
        url = reverse('v1:contacts-list')

        response = self.client.post(url, self.dummy_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, self.dummy_data)
