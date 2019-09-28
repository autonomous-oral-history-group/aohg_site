# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import netifaces
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name): 
    try: 
        return os.environ[var_name] 
    except KeyError: 
        #error_msg = msg % var_name 
        error_msg = var_name 
        raise ImproperlyConfigured(error_msg) 
        pass

# Find out what the IP addresses are at run time
# This is necessary because otherwise Gunicorn will reject the connections
# Allow Django from all hosts. This snippet is installed from
# /var/lib/digitalocean/allow_hosts.py 
def ip_addresses():
    ip_list = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        for x in (netifaces.AF_INET, netifaces.AF_INET6):
            if x in addrs:
                ip_list.append(addrs[x][0]['addr'])
    return ip_list

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable('DJANGO_SECRET_KEY')

APPEND_SLASH = True

# Application definition
INSTALLED_APPS = (
    'names.apps.NamesConfig',
	 'recordings.apps.RecordingsConfig',
	 'pages.apps.PagesConfig',
	 'sidebars.apps.SidebarsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
	 'audiofield',
	 'tinymce',
	 'tagulous',
	 'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', 
	 'audiofield.middleware.threadlocals.ThreadLocals',
)

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

TINYMCE_DEFAULT_CONFIG = {
    'plugins': "autolink,table,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '../static/')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
	("css", os.path.join(BASE_DIR, '../front_end/css')),
	("assets", os.path.join(BASE_DIR, '../front_end/assets')),
    ("js", os.path.join(BASE_DIR, '../front_end/js'))
]



SERIALIZATION_MODULES = {
    'xml':    'tagulous.serializers.xml_serializer',
    'json':   'tagulous.serializers.json',
    'python': 'tagulous.serializers.python',
    'yaml':   'tagulous.serializers.pyyaml',
} 


TAGULOUS_NAME_MAX_LENGTH = 255
TAGULOUS_SLUG_MAX_LENGTH = 50
TAGULOUS_LABEL_MAX_LENGTH = TAGULOUS_NAME_MAX_LENGTH


#-----
# Settings for django-audiofile
# Set Following variable
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'



# Frontend widget values
# 0-Keep original, 1-Mono, 2-Stereo
CHANNEL_TYPE_VALUE = 0

# 0-Keep original, 8000-8000Hz, 16000-16000Hz, 22050-22050Hz,
# 44100-44100Hz, 48000-48000Hz, 96000-96000Hz
FREQ_TYPE_VALUE = 8000

# 0-Keep original, 1-Convert to MP3, 2-Convert to WAV, 3-Convert to OGG
CONVERT_TYPE_VALUE = 0

# https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html
EMAIL_HOST = get_env_variable('EMAIL_SMTP')
EMAIL_PORT = 587
EMAIL_HOST_USER = get_env_variable('EMAIL_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_PASS')
EMAIL_USE_TLS = True 

