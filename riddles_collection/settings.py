import os
import sys

PROJECT_DIR = os.path.dirname(__file__)

#TODO: calculate how many times this module has imported
sys.path.append(os.path.join(PROJECT_DIR, '../'))

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'riddles',
        'USER': 'riddles',
        'PASSWORD': 'riddles',
        'HOST': '',
        'PORT': '',
    }
}

#TODO: UTC
TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

# MEDIA_ROOT = ''
# MEDIA_URL = ''

STATIC_URL = '/static/'
STATICFILES_DIRS = ( os.path.join(PROJECT_DIR, 'static'), )

ADMIN_MEDIA_PREFIX = '/static/admin/'

LESS_CSS_URL = '/less/'
LESS_FILES_DIR = os.path.join(PROJECT_DIR, 'less')
LESS_DEST_DIR = os.path.join(PROJECT_DIR, 'static', 'css')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '2oxoy51-(z0mhjk^ow=7_hy92o@k!pv(td3to(pg@nd9)d89_t'

APPEND_SLASH = True

#TODO: jinja
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django_next.less.context_processors.less',
    'utils.context_processors.categories'
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'riddles_collection.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles', # TODO: remove if not in DEBUG mode

    'utils',
    'riddles',

    'south',

    'django_next.less'
)


try:
    from settings_local import *
except:
    pass

TEMPLATE_DEBUG = DEBUG

if not DEBUG:
    LESS_CSS_URL = '%scss/' % STATIC_URL
