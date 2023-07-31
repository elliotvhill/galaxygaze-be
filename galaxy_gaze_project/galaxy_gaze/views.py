from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .seed import seed_astro_bodies, get_astro_bodies
from django.shortcuts import render
from rest_framework import generics
from .models import CelestialBody, CosmicEvent, User, DeepSpaceObject
from .serializers import CelestialBodySerializer, CosmicEventSerializer, UserSerializer, DeepSpaceObjectSerializer

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
class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    read_only=False

# user detail
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    read_only=False

# deep space object list
class DeepSpaceObjectList(generics.ListCreateAPIView):
    queryset = DeepSpaceObject.objects.all()
    serializer_class = DeepSpaceObjectSerializer
    read_only=False

# deep space object detail
class DeepSpaceObjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeepSpaceObject.objects.all()
    serializer_class = DeepSpaceObjectSerializer
    read_only=False

# view deep space search result
@require_GET
def deepspaceobject_view(request):
    try:
        term = request.GET.get('term', '')
        
        # term search, case insensitive:
        search_results = DeepSpaceObject.objects.filter(object_name__icontains=term)
        serializer = DeepSpaceObjectSerializer(search_results, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)