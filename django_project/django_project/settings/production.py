"""
Django settings for django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Discover our IP address
#ALLOWED_HOSTS = ip_addresses()
#ALLOWED_HOSTS += ['aohistorygroup.com']
ALLOWED_HOSTS = ['oralhistorygroup.com', 'www.oralhistorygroup.com', 'aohistorygroup.com', 'www.aohistorygroup.com',  'aohistorygroup.com', '134.209.59.89', '127.0.0.1']
ALLOWED_HOSTS += ip_addresses()

APPEND_SLASH = True

WSGI_APPLICATION = 'django_project.wsgi.application'

#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

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


AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_env_variable('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = get_env_variable('AWS_S3_REGION_NAME')
AWS_S3_ENDPOINT_URL = get_env_variable('AWS_S3_ENDPOINT_URL')

S3_URL = get_env_variable('AWS_S3_CUSTOM_DOMAIN')



#MEDIA_URL = '/media/'
MEDIA_URL = '%smedia/' % S3_URL


MEDIA_ROOT = 'media/'
#MEDIA_ROOT = os.path.join(BASE_DIR,'media/'


#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'django_project.settings.storage_backends.MediaStorage'
