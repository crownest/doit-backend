# Local Django
from .base_api_views import ContactViewSet
from core.serializers import ContactSerializer, ContactCreateSerializerV1


class ContactViewSetV1(ContactViewSet):

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactCreateSerializerV1
        else:
            return ContactSerializer
