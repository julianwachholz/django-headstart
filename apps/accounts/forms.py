# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth

from .models import User


class UserCreateForm(forms.ModelForm):
    """
    Create a new user account.

    """
    password = forms.CharField(label=_('Password'))

    class Meta:
        model = User
        fields = ['email']

    def save(self, commit=True):
        self.user = super(UserCreateForm, self).save(commit=False)
        self.user.set_password(self.cleaned_data['password'])

        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(forms.Form):
    """
    Verify the user's current password and set a new one.

    """
    ERRORS = {
        'current_password': _('Current password is not correct.'),
    }

    current_password = forms.CharField(label=_('Current password'), widget=forms.PasswordInput)
    password = forms.CharField(label=_('New password'))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PasswordChangeForm, self).__init__(*args, **kwargs)

    def clean_current_password(self):
        password = self.cleaned_data['current_password']
        if not self.user.check_password(password):
            raise forms.ValidationError(self.ERRORS['current_password'])
        return True

    def save(self):
        password = self.cleaned_data['password']
        self.user.set_password(password)
        self.user.save()
