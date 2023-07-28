from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, default='exampleUser')
    user_email = models.CharField(max_length=100, default='example@example.com')
    user_password = models.CharField(max_length=30, default='password')
    followed_bodies = models.ManyToManyField('CelestialBody', blank=True)
    followed_events = models.ManyToManyField('CosmicEvent', blank=True)

    def __str__(self):
        return self.username

class CelestialBody(models.Model):
    name = models.CharField()
    distanceFromEarth = models.BigIntegerField(blank=True) # allowing field to be blank while in dev
    horizontal_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    horizon_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    equatorial_pos = models.CharField(blank=True) # allowing field to be blank while in dev
    extra_info = models.CharField(blank=True) # allowing field to be blank while in dev

    def __str__(self):
        return self.name
    
class CosmicEvent(models.Model):
    event_name = models.CharField(blank=True)
    event_date = models.CharField(blank=True)
    event_description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name

class DeepSpaceObject(models.Model):
    object_name = models.CharField(blank=True)
    object_type = models.CharField(blank=True)
    object_sub_type = models.CharField(blank=True)
    object_position_ra = models.CharField(blank=True)
    object_position_dec = models.CharField(blank=True)

    def __str__(self):
        return self.object_name
