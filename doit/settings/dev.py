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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DOMAIN = 'http://127.0.0.1:8000'

from .local import *
