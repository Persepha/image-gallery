from .base import *

DEBUG = False

DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAILABLE = all([
    DB_DATABASE,
    DB_PASSWORD,
    DB_USERNAME,
    DB_HOST,
    DB_PORT,
])

# POSTGRES_READY = int(os.environ.get("POSTGRES_READY"))

if DB_IS_AVAILABLE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_DATABASE,
            'USER': DB_USERNAME,
            'PASSWORD': DB_PASSWORD,
            'HOST': DB_HOST,
            'PORT': DB_PORT,
        }
    }


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
