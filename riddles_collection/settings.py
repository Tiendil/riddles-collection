# coding: utf-8

import os
import sys
from dext.utils.meta_config import MetaConfig

TESTS_RUNNING = 'test' in sys.argv or 'testserver' in sys.argv

PROJECT_DIR = os.path.dirname(__file__)

meta_config = MetaConfig(config_path=os.path.join(PROJECT_DIR, 'meta_config.json'))

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

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'ru'

SITE_ID = 1
SITE_URL = 'zagadki.org'

X_FRAME_OPTIONS = 'DENY'

##############################
# I18N
##############################

USE_I18N = True
USE_L10N = True

##############################
# static content settings
##############################

STATIC_URL = '/static/%s/' % meta_config.static_data_version
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

DCONT_URL = '/dcont/'
DCONT_DIR = os.path.join(PROJECT_DIR, 'dcont')

LESS_CSS_URL = STATIC_URL + 'less/'
LESS_FILES_DIR = os.path.join(PROJECT_DIR, 'less')
LESS_DEST_DIR = os.path.join(PROJECT_DIR, 'static', 'css')

SECRET_KEY = '2oxoy51-(z0mhjk^ow=7_hy92o@k!pv(td3to(pg@nd9)d89_t'

GA_CODE = 'UA-10915391-1'

################################
# Mail settings
################################

SERVER_EMAIL = 'a.eletsky@gmail.com'
ADMINS = (('Tiendil', 'a.eletsky@gmail.com'), )

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

################################
# Other settings
################################

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
    'dext.less.context_processors.less',
    'utils.context_processors.categories'
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

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

    'utils',

    'portal',

    'riddles',

    'south',

    'dext.less'
)

try:
    from settings_local import *
except:
    pass

if 'TEMPLATE_DEBUG' not in globals():
    TEMPLATE_DEBUG = DEBUG

if not DEBUG:
    LESS_CSS_URL = '%scss/' % STATIC_URL

############################
# LOGGING
############################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s %(asctime)s %(module)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
            }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    } if not TESTS_RUNNING else {}
}
