from .base import *

# SECURITY WARNING: don't run with debug turned on in production!  
DEBUG = True

ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
		  'NAME': get_env_variable('DATABASE_NAME'),
		  'USER': get_env_variable('DATABASE_USER'),
		  'PASSWORD' : get_env_variable('DATABASE_PASSWORD')
    }
}


STATIC_ROOT = os.path.join(BASE_DIR, get_env_variable('STATIC_ROOT'))
