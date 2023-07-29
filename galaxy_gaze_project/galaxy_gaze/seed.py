import requests
from django.core.management.base import BaseCommand
from galaxy_gaze.models import CelestialBody, DeepSpaceObject
# CosmicEvent, User
import os
from dotenv import load_dotenv
load_dotenv()
# DEBUG = os.getenv('DEBUG', False)
DJANGO_WEATHER_API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')
DJANGO_ASTRO_DATABASE_URL = os.getenv('DJANGO_ASTRO_DATABASE_URL')
NETLIFY_ASTRO_APP_ID = os.getenv('NETLIFY_ASTRO_APP_ID')
NETLIFY_ASTRO_APP_SECRET = os.getenv('NETLIFY_ASTRO_APP_SECRET')
DJANGO_ASTRO_DEMO_AUTH_STR = os.getenv('DJANGO_ASTRO_DEMO_AUTH_STR')
DJANGO_ASTRO_DEEP_SPACE_URL = os.getenv('DJANGO_ASTRO_DEEP_SPACE_URL')
AUTH_STRING = f"{NETLIFY_ASTRO_APP_ID}:{NETLIFY_ASTRO_APP_SECRET}"


# API REQUESTS:

# request for specific deep space object:
def deepspaceobject(command_instance, term, match_type, limit, offset):
    # headers = { 'Authorization': f"Basic {AUTH_STRING}", 'Access-Control-Allow-Origin': "https://galaxygaze.netlify.app" }
    # headers = { 'Authorization': f"Basic {DJANGO_ASTRO_DEMO_AUTH_STR}", 'Access-Control-Allow-Origin': "http://localhost:5173" }
    headers = { 'Authorization': f"Basic {DJANGO_ASTRO_DEMO_AUTH_STR}" }
    url = DJANGO_ASTRO_DEEP_SPACE_URL
    params = {
        'term': term,
        'match_type': match_type,
        'limit': limit,
        'offset': offset
    }
    search_results = []

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        object = response.json()
        print(object)
        if object['data']:
            api_object_data = object['data'][0]

            object_name = api_object_data['name']
            object_type = api_object_data['type']['name']
            object_sub_type = api_object_data['subType']['name']
            object_position_ra = api_object_data['position']['equatorial']['rightAscension']['string']
            object_position_dec = api_object_data['position']['equatorial']['declination']['string']

            # create and save new instance of deep space object:
            deepspaceobject = DeepSpaceObject(
                object_name = object_name,
                object_type = object_type,
                object_sub_type = object_sub_type,
                object_position_ra = object_position_ra,
                object_position_dec = object_position_dec
            )
            deepspaceobject.save()

            # Append the result to the search_results list
            result = {
                'object_name': object_name,
                'object_type': object_type,
                'object_sub_type': object_sub_type,
                'object_position_ra': object_position_ra,
                'object_position_dec': object_position_dec
            }
            search_results.append(result)
            pass
        
        else:
            print('No data found')
    else:
        print('API request failed')


# clear data to prevent duplicates if need to re-seed
def clear_data():
    #  CelestialBody.objects.all().delete()
    DeepSpaceObject.objects.all().delete()

# command class to extend BaseCommand and call functions
class Command(BaseCommand):
     def add_arguments(self, parser):
        parser.add_argument('term', type=str, help='Search term for deep space objects')

     def handle(self, *args, **options):
        term = options['term']
        match_type = 'fuzzy'
        limit = '10'
        offset = '0'
        deepspaceobject(self, term, match_type, limit, offset)
        # clear_data()
        print(f"Data seeding for term {term} completed")