from rest_framework import serializers
from .models import CelestialBody, CosmicEvent, User, DeepSpaceObject

class CelestialBodySerializer(serializers.HyperlinkedModelSerializer):
    cosmic_events = serializers.HyperlinkedRelatedField(
        view_name='event_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = CelestialBody
        fields = ('id', 'name', 'distanceFromEarth', 'horizontal_pos', 'horizon_pos', 'equatorial_pos', 'extra_info')


class CosmicEventSerializer(serializers.HyperlinkedModelSerializer):
    celestial_body = serializers.HyperlinkedRelatedField(
        view_name='body_detail',
        many=True,
        queryset=CelestialBody.objects.all()
    )
    class Meta:
        model = CosmicEvent
        fields = ('id', 'event_name', 'event_date', 'event_description')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    followed_bodies = CelestialBodySerializer(many=True, read_only=True)
    followed_events = CosmicEventSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'user_email', 'followed_bodies', 'followed_events')


class DeepSpaceObjectSerializer(serializers.HyperlinkedModelSerializer):
    space_object = serializers.HyperlinkedRelatedField(
        view_name='deep_space_object',
        many=True,
        read_only=True
    )

    class Meta:
        model: DeepSpaceObject
        fields = ('id', 'object_name', 'object_type', 'object_position')