# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from core.models import Contact
from core.serializers import ContactSerializer, ContactCreateSerializer


class ContactViewSet(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Contact.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return ContactCreateSerializer
        else:
            return ContactSerializer

    def get_permissions(self):
        permissions = super(ContactViewSet, self).get_permissions()

        if self.action == 'create':
            return []

        return permissions
