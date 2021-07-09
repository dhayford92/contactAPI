from contants.serializers import ContactSerializer
from contants.models import Contact
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class ContactList(ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateAPIView):
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated, )
    lookup_field = "id"

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)