from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from events.models import Event
from events.serializers import EventsSerializer


class EventsView(APIView):

    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventsSerializer(events)
        return Response(serializer.data)
