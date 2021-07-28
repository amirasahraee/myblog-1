from rest_framework.generics import CreateAPIView
from ..serializer import ContactUsSerializer
from rest_framework.permissions import AllowAny


class ContactUsView(CreateAPIView):
    serializer_class = ContactUsSerializer
    permission_classes = [AllowAny]
