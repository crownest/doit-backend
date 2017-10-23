# Third-Party
from rest_framework import serializers

# Local Django
from core.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email', 'message')


class ContactCreateSerializer(ContactSerializer):

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')
