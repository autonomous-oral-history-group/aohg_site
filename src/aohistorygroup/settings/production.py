from .base import *

# SECURITY WARNING: don't run with debug turned on in production!  
DEBUG = False

ALLOWED_HOSTS = ['aohistorygroup.com']

# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
		  'NAME': get_env_variable('DATABASE_NAME'),
		  'USER': get_env_variable('DATABASE_USER'),
		  'PASSWORD' : get_env_variable('DATABASE_PASSWORD')
    }
}


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

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
