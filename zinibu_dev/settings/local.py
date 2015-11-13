from .base import *

DEBUG = True

if get_env_variable('PROJECT_DATABASES_ENGINE') == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, get_env_variable('PROJECT_DATABASES_DEFAULT_NAME')),
        }
    }
elif get_env_variable('PROJECT_DATABASES_ENGINE') == 'postgresql':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_env_variable('PROJECT_DATABASES_DEFAULT_NAME'),
            'USER': get_env_variable('PROJECT_DATABASES_DEFAULT_USER'),
            'PASSWORD': get_env_variable('PROJECT_DATABASES_DEFAULT_PASSWORD'),
            'HOST': get_env_variable('PROJECT_DATABASES_DEFAULT_HOST'),
            'PORT': get_env_variable('PROJECT_DATABASES_DEFAULT_PORT'),
        }
    }
