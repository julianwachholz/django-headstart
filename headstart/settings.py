# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
"""
Django settings for project {{ project_name }}.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

"""
import os
import environ
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _


BASE_DIR = environ.Path(__file__) - 2

# Environment utility with default values
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(BASE_DIR.file('.env'))


DEBUG = env('DEBUG')
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = env('SECRET_KEY')

# TODO: add hosts to ALLOWED_HOSTS
ALLOWED_HOSTS = [
    '.example.com',
]


# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRDPARTY_APPS = [
    'sniplates',

    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'two_factor',
]

if DEBUG:
    THIRDPARTY_APPS += [
        'debug_toolbar',
    ]
else:
    THIRDPARTY_APPS += [
        'raven.contrib.django.raven_compat',
    ]

PROJECT_APPS = [
    'apps.accounts',
    'utils',
]

INSTALLED_APPS = DJANGO_APPS + THIRDPARTY_APPS + PROJECT_APPS

if not DEBUG:
    RAVEN_CONFIG = {
        'dsn': env('SENTRY_DSN'),
    }


MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_USER_MODEL = 'accounts.User'

ACCOUNT_VERIFY_EMAIL = False
ACCOUNT_VERIFICATION_DAYS = 3

PASSWORD_RESET_TIMEOUT_DAYS = 3

# TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.twilio.gateway.Twilio'
# if DEBUG:
#     TWO_FACTOR_SMS_GATEWAY = 'two_factor.gateways.fake.Fake'

ROOT_URLCONF = 'headstart.urls'
LOGIN_URL = 'two_factor:login'
LOGOUT_URL = 'accounts:logout'
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'headstart.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': env.db_url(),
}

CACHES = {
    'default': env.cache_url(),
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

if DEBUG:
    # `runserver` will lose our session on each code reload otherwise
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'


DEFAULT_FROM_EMAIL = 'info@django-headstart'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR('locale'),
]


TEMPLATE_DIRS = [
    BASE_DIR('templates'),
]

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    # 'utils.context_processors.url_info',
]


if not DEBUG:
    TEMPLATE_LOADERS = [
        ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
    ]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR('assets'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = env('MEDIA_ROOT', default=BASE_DIR('media'))


CSRF_COOKIE_HTTPONLY = True
# Set to True on HTTPS enabled sites!
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'two_factor': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}
