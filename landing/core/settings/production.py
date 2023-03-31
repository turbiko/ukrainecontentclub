from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
print('DEBUG.dev= ', DEBUG)
DEBUG404 = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "dm*#_9rs0r0z$g)65#m12y6wxl@rpw$%1dxu@+(x^dm*#_9rs0r0z$g)65#m12y6wv!=2b%"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME":   os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

try:
    from .local import *
except ImportError:
    pass
