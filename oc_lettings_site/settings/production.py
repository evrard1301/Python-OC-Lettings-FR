import os
from oc_lettings_site.settings.base import *

SECRET_KEY = os.getenv('OC_SECRET') 

DEBUG = False

ALLOWED_HOSTS = []

