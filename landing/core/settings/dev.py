import os
from .base import *
from django.core.management import utils

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print('DEBUG.dev= ', DEBUG)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.path.dirname(PROJECT_DIR)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://a1.ukrainecontentclub.com.ua/', 'https://ukrainecontentclub.com.ua/']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
