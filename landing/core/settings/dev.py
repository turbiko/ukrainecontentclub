import os
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print('DEBUG.dev= ', DEBUG)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)7ywpo%3%wx%-t4#25a!hgz*ub%p)njx()%*5&z$0kkf)j9d37"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
