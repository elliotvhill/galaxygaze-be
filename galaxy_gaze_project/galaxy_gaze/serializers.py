from rest_framework import serializers
from .models import CelestialBody, CosmicEvent

class CelestialBodySerializer(serializers.HyperlinkedModelSerializer):
    cosmic_events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = CelestialBody
        fields = ('id', 'name', 'distanceFromEarth', 'horizontal_pos', 'horizon_pos', 'equatorial_pos', 'extra_info')