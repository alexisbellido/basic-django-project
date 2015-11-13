from .base import *

DEBUG = True

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, get_env_variable("PROJECT_DATABASES_DEFAULT_NAME")),
#    }
#}

# TODO get from env vars
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db1',
        'USER': 'user1',
        'PASSWORD': 'user_secret',
        'HOST': '192.168.1.10',
        'PORT': '5432',
    }
}
