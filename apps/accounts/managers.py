# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """
    Manager for the most-basic user model.

    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.

        """
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
