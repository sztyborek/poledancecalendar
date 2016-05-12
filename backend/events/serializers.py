from rest_framework import serializers
from models import Event

class EventsSerializer(object):
    class Meta:
        model = Event
        fields = ('pk', 'date', 'status', 'facebook_event', 'contact_email', 'category')
