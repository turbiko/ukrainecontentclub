from .base import *
from django.core.management import utils

DEBUG = False



CORS_ORIGIN_ALLOW_ALL = True


try:
    from .local import *
except ImportError:
    pass
