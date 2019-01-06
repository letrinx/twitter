from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%jcq*to#n&idf@!@wec#!de@#5124%$23$RfG5$YDFGcXVQ2$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twitter',
        'USER': 'PROD',
        'PASSWORD': 'PROD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}