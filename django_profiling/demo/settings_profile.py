from default_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demo.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
DEBUG = True
TEMPLATE_DEBUG = True
PROFILING = True
STATIC_ROOT = 'static_root'

INTERNAL_IPS = ('127.0.0.1',)
INSTALLED_APPS += (
)
MIDDLEWARE_CLASSES += (
    'depiction.middleware.ProfilerMiddleware',
)