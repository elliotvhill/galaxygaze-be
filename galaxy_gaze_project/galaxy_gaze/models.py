from django.db import models
import requests
import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = os.getenv('DEBUG', False)
DJANGO_WEATHER_API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')
DJANGO_ASTRO_DATABASE_URL = os.getenv('DJANGO_ASTRO_DATABASE_URL')
DJANGO_ASTRO_APP_ID = os.getenv('DJANGO_ASTRO_APP_ID')
DJANGO_ASTRO_APP_SECRET = os.getenv('DJANGO_ASTRO_APP_SECRET')

# MODEL DEFINITIONS:

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
    event_name = models.CharField()
    event_date = models.CharField()
    event_description = models.TextField()

    def __str__(self):
        return self.event_name


# API REQUESTS:

def get_astro_bodies():
    url = DJANGO_ASTRO_DATABASE_URL
    response = request.get(url)

    if response.status_code == 200:
        data = response.json()

        celestial_bodies_data = data.get('data', {}).get('table', {}).get('rows', [])
        for celest_body_data in celestial_bodies_data:
            # extract data from API response
            name=celest_body_data.get('entry', {}).get('name')
            distance_from_earth=celest_body_data.get('cells', [{}])[0].get('distance', {}).get('fromEarth', {}).get('km')
            horizontal_pos = celest_body_data.get('cells', [{}])[0].get('position', {}).get('horizontal', {}).get('altitude', {}).get('degrees')
            horizon_pos = celest_body_data.get('cells', [{}])[0].get('position', {}).get('horizonal', {}).get('altitude', {}).get('degrees')
            equatorial_pos = celest_body_data.get('cells', [{}])[0].get('position', {}).get('equatorial', {}).get('rightAscension', {}).get('hours')
            extra_info = celest_body_data.get('cells', [{}])[0].get('extraInfo', {}).get('magnitude')

            # create and save new instance CelestialBody
            celestial_body = CelestialBody(
                name=name,
                distanceFromEarch=distance_from_earth,
                horizontal_pos=horizontal_pos,
                horizon_pos=horizon_pos,
                equatorial_pos=equatorial_pos,
                extra_info=extra_info,
            )
            celestial_body.save()