from blog_app.settings.dev import ALLOWED_HOSTS, SECRET_KEY
from urllib import urlparse
from .base import *
from django.core.management.utils import get_random_secret_key

DEBUG = False

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key)
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split

r = urlparse(os.environ.get("DATABASE_URL"))

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.path.realpath(r.path, "/"),
        "USER": r.username,
        "PASSWORD": r.password,
        "HOST": r.hostname,
        "PORT": r.port,
        "OPTIONS": {"sslmode": "require"},
    }
}
