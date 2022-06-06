from .base import *
from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5ihj$x=zc_+4=d2uv4yaok633=sd=oyeq9!@tvz)_i9sz#7m$*'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "wagtail",
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", 5432),
        'OPTIONS': {
            'connect_timeout': 3,
            'sslmode': 'require'
        }
    }
}


try:
    from .local import *
except ImportError:
    pass
