import os
from .base import *
from django.core.management import utils

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print('DEBUG.dev= ', DEBUG)

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CORS_ORIGIN_ALLOW_ALL = True
try:
    from .local import *
except ImportError:
    pass
