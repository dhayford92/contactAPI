from contants.models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'country_code', 'first_name', 'last_name', 'contact_picture', 'phone_number', 'is_favorite']