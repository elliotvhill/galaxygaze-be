from django.contrib import admin
from .models import CelestialBody, CosmicEvent

admin.site.register(CelestialBody)
admin.site.register(CosmicEvent)