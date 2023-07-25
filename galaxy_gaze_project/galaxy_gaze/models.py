from django.db import models

class CelestialBody(models.Model):
    name = models.CharField()
    distanceFromEarth = models.BigIntegerField(blank=True) # allowing field to be blank while in dev
    horizontal_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    horizon_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    equatorial_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    extra_info = models.CharField(blank=True) # allowing field to be blank while in dev

    def __str__(self):
        return self.name