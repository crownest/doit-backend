# Third-Party
from rest_framework.test import APITestCase


class ContactAPITestCase(APITestCase):
    dummy_data = {
        'first_name': 'Doit',
        'last_name': 'Apps',
        'email': 'doit@unicrow.com',
        'message': 'Good job!'
    }
