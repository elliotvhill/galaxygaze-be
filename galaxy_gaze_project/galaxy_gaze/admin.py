from django.contrib import admin
from .models import User, CelestialBody, CosmicEvent

admin.site.register(User)
admin.site.register(CelestialBody)
admin.site.register(CosmicEvent)