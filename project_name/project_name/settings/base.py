# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from os import environ
from os.path import join, abspath, dirname

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

import dj_database_url


def get_env_setting(setting, default=None):
    """
    Get en environment setting or return its default value.

    Raises an exception if no default is supplied.

    """
    try:
        return environ[setting]
    except KeyError:
        if default is not None:
            return default
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


########## PATH CONFIGURATION
# Setting up paths
here = lambda *x: abspath(join(dirname(__file__), *x))

DJANGO_ROOT = here('..', '..')
root = lambda *x: abspath(join(DJANGO_ROOT, *x))
########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION
DEBUG = bool(get_env_setting('DEBUG', False))
TEMPLATE_DEBUG = DEBUG
INTERNAL_IPS = ('127.0.0.1',)
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
ADMINS = (
    ('John Doe', 'john.doe@example.com'),
)

MANAGERS = ADMINS
SERVER_EMAIL = 'system@localhost'
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
DEFAULT_DATABASE = 'sqlite:///{{ project_name }}.db'
DATABASES = {
    'default': dj_database_url.parse(get_env_setting('DATABASE_URL', DEFAULT_DATABASE)),
}
CONN_MAX_AGE = 60
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## GENERAL CONFIGURATION
USE_TZ = True
TIME_ZONE = 'UTC'

USE_I18N = True
LANGUAGE_CODE = 'en-us'
LANGUAGE_COOKIE_NAME = '{{ project_name }}_language'
LANGUAGES = (
    ('en', _('English')),
)

USE_L10N = True
FIRST_DAY_OF_WEEK = 1  # Monday
########## END GENERAL CONFIGURATION


########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
MANDRILL_API_KEY = get_env_setting('MANDRILL_API_KEY', 'dummy')
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'team@localhost'
########## END EMAIL CONFIGURATION


########## MEDIA CONFIGURATION
MEDIA_ROOT = root('media')
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
STATIC_ROOT = root('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    root('assets'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECURITY CONFIGURATION
SECRET_KEY = get_env_setting('SECRET_KEY', 'dummy' if DEBUG else None)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
)

SESSION_COOKIE_NAME = '{{ project_name }}_session'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 2  # 2 days
# TODO make sure to configure SSL
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

PASSWORD_RESET_TIMEOUT_DAYS = 3
########## END SECURITY CONFIGURATION


########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
ALLOWED_HOSTS = get_env_setting('ALLOWED_HOSTS', 'localhost').split()
########## END SITE CONFIGURATION


########## FIXTURE CONFIGURATION
FIXTURE_DIRS = (
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    root('templates'),
)
########## END TEMPLATE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
ROOT_URLCONF = '{{ project_name }}.urls.base'
if DEBUG:
    ROOT_URLCONF = '{{ project_name }}.urls.local'
ABSOLUTE_URL_OVERRIDES = {}

#LOGIN_URL = 'accounts:login'
#LOGOUT_URL = 'accounts:logout'
#LOGIN_REDIRECT_URL = 'accounts:myaccount'
########## END URL CONFIGURATION


########## APP CONFIGURATION
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.gis',

    'south',

    # 'apps.myapp',
)

if not DEBUG:
    INSTALLED_APPS += (
        'djrill',
    )
else:
    # remove comments to enable the debug toolbar
    # disabled by default to prevent premature optimization
    INSTALLED_APPS += (
        # 'debug_toolbar',
        # 'template_timings_panel',
    )
########## END APP CONFIGURATION


########## APP SETTINGS
# add app specific settings here
########## END APP SETTINGS


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'
########## END WSGI CONFIGURATION


########## DEBUG TOOLBAR CONFIGURATION
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)
########## END DEBUG TOOLBAR CONFIGURATION
