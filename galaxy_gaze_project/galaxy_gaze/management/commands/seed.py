import requests
from django.core.management.base import BaseCommand
from galaxy_gaze.models import CelestialBody 
# CosmicEvent, User
import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = os.getenv('DEBUG', False)
DJANGO_WEATHER_API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')
DJANGO_ASTRO_DATABASE_URL = os.getenv('DJANGO_ASTRO_DATABASE_URL')
DJANGO_ASTRO_APP_ID = os.getenv('DJANGO_ASTRO_APP_ID')
DJANGO_ASTRO_APP_SECRET = os.getenv('DJANGO_ASTRO_APP_SECRET')
ASTRO_DEMO_AUTH_STR = os.getenv('ASTRO_DEMO_AUTH_STR')
# AUTH_STRING = f"({DJANGO_ASTRO_APP_ID}:{DJANGO_ASTRO_APP_SECRET})"


# API REQUESTS:

def get_astro_bodies(latitude, longitude, from_date, to_date, time, page_size=10, max_pages=2):
    url = DJANGO_ASTRO_DATABASE_URL
    page = 1
    total_pages = None
    while page <= max_pages:
        params = {
            'latitude': latitude,
            'longitude': longitude,
            'from_date': from_date,
            'to_date': to_date,
            'time': time,
            'page': page,
            'page_size': page_size,
            }
        response = requests.get(url, params=params, headers={'Authorization': f"Basic {ASTRO_DEMO_AUTH_STR}"})
        if response.status_code == 200:
            astro_bodies = response.json()
            print(astro_bodies)
            # return astro_bodies
            celestial_bodies_data = astro_bodies.get('data', {}).get('table', {}).get('rows', [])
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

            if total_pages is None:
                total_pages = astro_bodies.get('data', {}).get('table', {}).get('total_pages', 1)
                page += 1
        else:
            print(f"Error fetching data. Status code: {response.status_code}")
            break

# clear data to prevent duplicates if need to re-seed
def clear_data():
     CelestialBody.objects.all().delete()

# hardcoding user spacetime data for testing:
latitude = '40.7128'
longitude = '-74.0060'
from_date = '2023-07-24'
to_date = '2023-07-24'
time = '12:00:00'

# command class to extend BaseCommand and call functions
class Command(BaseCommand):

     def handle(self, *args, **options):
          get_astro_bodies(latitude, longitude, from_date, to_date, time)
          clear_data()
          print("completed")