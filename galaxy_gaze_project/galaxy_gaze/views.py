from django.shortcuts import render
from rest_framework import generics
from .models import CelestialBody, CosmicEvent
from .serializers import CelestialBodySerializer, CosmicEventSerializer

# bodies list
class BodiesList(generics.ListCreateAPIView):
    queryset = CelestialBody.objects.all()
    serializer_class = CelestialBodySerializer
    read_only=True

# body detail
class BodyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CelestialBody.objects.all()
    serializer_class = CelestialBodySerializer
    read_only=True

# events list
class EventsList(generics.ListCreateAPIView):
    queryset = CosmicEvent.objects.all()
    serializer_class = CosmicEventSerializer
    read_only=True

# event detail
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CosmicEvent.objects.all()
    serializer_class = CosmicEventSerializer
    read_only=True

# users list

# user detail