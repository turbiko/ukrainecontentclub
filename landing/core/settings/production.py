from .base import *
from django.core.management import utils

DEBUG = False
print('DEBUG.prod= ', DEBUG)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["127.0.0.1", "ukrainecontentclub.com.ua"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

CORS_ORIGIN_ALLOW_ALL = True

try:
    from .local import *
except ImportError:
    pass
