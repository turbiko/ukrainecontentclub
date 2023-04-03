from .base import *
from django.core.management import utils

DEBUG = False
print('DEBUG.prod= ', DEBUG)





try:
    from .local import *
except ImportError:
    pass
