# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


@python_2_unicode_compatible
class User(AbstractBaseUser, PermissionsMixin):
    """
    Basic admin-compatible user model
    with email and password.

    """
    email = models.EmailField(_('email'), unique=True)
    is_active = models.BooleanField(_('active'), default=True)
    created = models.DateTimeField(_('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['email']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser

    def get_short_name(self):
        return self.email
