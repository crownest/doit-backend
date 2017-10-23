# Third-Party
from rest_framework import viewsets, mixins

# Local Django
from users.models import User
from core.models import Contact
from doit.modules import MailModule
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

    def perform_create(self, serializer):
        contact = serializer.save()

        # Send Contact Mail
        users = User.objects.filter(is_superuser=True)
        for user in users:
            MailModule.send_contact_mail(contact, user)
