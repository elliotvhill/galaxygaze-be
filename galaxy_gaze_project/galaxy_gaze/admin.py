from django.contrib import admin
from .models import User, CelestialBody, CosmicEvent, DeepSpaceObject

admin.site.register(User)
admin.site.register(CelestialBody)
admin.site.register(CosmicEvent)
admin.site.register(DeepSpaceObject)