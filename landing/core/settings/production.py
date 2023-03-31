from .base import *
from django.core.management import utils

DEBUG = False
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://a1.ukrainecontentclub.com.ua/', 'https://ukrainecontentclub.com.ua/']
SECRET_KEY = os.path.dirname(PROJECT_DIR)

try:
    from .local import *
except ImportError:
    pass
