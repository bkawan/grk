from .settings import *

SECRET_KEY = 'o!1(koazyhcbtl9y8tiawqh-0q_7m@rxj(!g1*o#ox&^^5kou*'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'grk.awecode.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pesatag',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', '..', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '..', "static"),
]