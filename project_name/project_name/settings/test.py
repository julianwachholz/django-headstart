# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }
}

# Use a quick password hasher
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
)

TEST_DISCOVER_TOP_LEVEL = DJANGO_ROOT
TEST_DISCOVER_ROOT = DJANGO_ROOT
TEST_DISCOVER_PATTERN = 'test_*'
