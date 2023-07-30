import requests
import os
import base64
from django.core.management.base import BaseCommand
from .models import CelestialBody, CosmicEvent, User, DeepSpaceObject
from dotenv import load_dotenv
load_dotenv()
DEBUG = os.getenv('DEBUG', False)
DJANGO_WEATHER_API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')
DJANGO_ASTRO_DATABASE_URL = os.getenv('DJANGO_ASTRO_DATABASE_URL')
NETLIFY_ASTRO_APP_ID = os.getenv('NETLIFY_ASTRO_APP_ID')
NETLIFY_ASTRO_APP_SECRET = os.getenv('NETLIFY_ASTRO_APP_SECRET')
AUTH_STRING = f"{NETLIFY_ASTRO_APP_ID}:{NETLIFY_ASTRO_APP_SECRET}"
ASTRO_CREDS_ENCODED = base64.b64encode(AUTH_STRING.encode()).decode('utf-8')


# API REQUESTS:

def get_astro_bodies():
    url = DJANGO_ASTRO_DATABASE_URL
    response = requests.get(url, headers={'Authorization':
                                         f"Basic Buffer.from({AUTH_STRING}).toString('base64')"})
    if response.status_code == 200:
        astro_bodies = response.json
    return astro_bodies

def seed_astro_bodies():
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

# clear data to prevent duplicates if need to re-seed
def clear_data():
     CelestialBody.objects.all().delete()

# command class to extend BaseCommand and call functions
class Command(BaseCommand):
     def handle(self, *args, **options):
          seed_astro_bodies()
          # clear_data()
          print("completed")














# import requests
# import base64
# from django.core.management.base import BaseCommand
# from galaxy_gaze.models import CelestialBody, DeepSpaceObject
# # CosmicEvent, User
# import os
# from dotenv import load_dotenv
# load_dotenv()
# # DEBUG = os.getenv('DEBUG', False)
# DJANGO_WEATHER_API_KEY = os.getenv('DJANGO_WEATHER_API_KEY')
# DJANGO_ASTRO_DATABASE_URL = os.getenv('DJANGO_ASTRO_DATABASE_URL')
# # DJANGO_ASTRO_DEMO_AUTH_STR = os.getenv('DJANGO_ASTRO_DEMO_AUTH_STR')
DJANGO_ASTRO_DEEP_SPACE_URL = os.getenv('DJANGO_ASTRO_DEEP_SPACE_URL')
# NETLIFY_ASTRO_APP_ID = os.getenv('NETLIFY_ASTRO_APP_ID')
# NETLIFY_ASTRO_APP_SECRET = os.getenv('NETLIFY_ASTRO_APP_SECRET')
# AUTH_STRING = f"{NETLIFY_ASTRO_APP_ID}:{NETLIFY_ASTRO_APP_SECRET}"
# ASTRO_CREDS_ENCODED = base64.b64encode(AUTH_STRING.encode()).decode('utf-8')


# # API REQUESTS:

# # request for specific deep space object:
def deepspaceobject(command_instance, term, match_type, limit, offset):
    headers = { "Accept": "*/*", 'Authorization': f"Basic {ASTRO_CREDS_ENCODED}", }
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
        # print(object)
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
            # result = {
            #     'object_name': object_name,
            #     'object_type': object_type,
            #     'object_sub_type': object_sub_type,
            #     'object_position_ra': object_position_ra,
            #     'object_position_dec': object_position_dec
            # }
            # search_results.append(result)
            pass
        
        else:
            print('No data found')
    else:
        print('API request failed')


# # clear data to prevent duplicates if need to re-seed
def clear_data():
#     #  CelestialBody.objects.all().delete()
    DeepSpaceObject.objects.all().delete()

# # command class to extend BaseCommand and call functions
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