from .base import *
from django.core.management import utils

DEBUG = False

SECRET_KEY = os.path.dirname(PROJECT_DIR)

try:
    from .local import *
except ImportError:
    pass
