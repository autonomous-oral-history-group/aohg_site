"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

"""

from .base import *


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Discover our IP address
#ALLOWED_HOSTS += ['aohistorygroup.com']
#ALLOWED_HOSTS = ['aohistorygroup.com', 'www.aohistorygroup.com',  'aohistorygroup.com', '134.209.59.89', '127.0.0.1']
#ALLOWED_HOSTS += ip_addresses()
ALLOWED_HOSTS = ip_addresses()


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
		  'NAME': get_env_variable('DATABASE_NAME'),
		  'USER': get_env_variable('DATABASE_USER'),
		  'PASSWORD' : get_env_variable('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}


