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



TINYMCE_DEFAULT_CONFIG = {
    'plugins': "autolink,table,paste,searchreplace",
    'theme': "advanced",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}

