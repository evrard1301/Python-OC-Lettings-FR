import os

SECRET_KEY = os.getenv('OC_SECRET')

DEBUG = False

ALLOWED_HOSTS = ['*']
