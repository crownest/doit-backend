# Local Django
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


ADMINS = (
    # ("Your Name", "your_email@example.com"),
)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/validators/

AUTH_PASSWORD_VALIDATORS = []


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'doitdb',
        'USER': 'doit',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '',
    }
}


DOMAIN = 'http://doit.unicrow.com'

from .local import *
