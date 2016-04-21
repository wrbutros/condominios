from defaults import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'condominios',
        'USER': 'django',
        'PASSWORD': 'condominios',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

ENVIRONMENT = 'devel'

CORS_ORIGIN_WHITELIST = (
    'condominio-transparente.dyndns.org'
)

STATIC_ROOT = os.path.join(BASE_DIR, "static/")