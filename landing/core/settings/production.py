from .base import *
from django.core.management import utils

DEBUG = False






try:
    from .local import *
except ImportError:
    pass
