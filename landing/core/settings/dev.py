import os
from .base import *
from django.core.management import utils

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
print('DEBUG.dev= ', DEBUG)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "dm*#_9rs0r0z$g)65#m12y6wxl@rpw$%1dxu@+(x^dm*#_9rs0r0z$g)65#m12y6wv!=2b%"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":   os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


DEBUG404 = False

try:
    from .local import *
except ImportError:
    pass
