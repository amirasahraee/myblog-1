from rest_framework.serializers import ModelSerializer
from ..models import ContactUs


class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['firstName', 'lastName', 'email', 'phone', 'message']
