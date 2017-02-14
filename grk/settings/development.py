from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
SECRET_KEY = 'o!1(koazyhcbtl9y8tiawqh-0q_7m@rxj(!g1*o#ox&^^5kou*'

ADMINS = (('Dipesh Acharya', 'dipesh@awecode.com'),)
MANAGERS = (('Dipesh Acharya', 'dipesh@awecode.com'),)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'pesatag',
#         'USER': 'postgres',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '',  # Set to empty string for default.
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SERVER_EMAIL = 'email@server.com'

AUTH_PASSWORD_VALIDATORS = []

# FIXME still not working ( according to github discussion
# FIXME ...it has issue with python3 )

