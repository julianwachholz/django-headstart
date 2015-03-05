# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_('Password'),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password below."))

    set_password = forms.CharField(
        label=_('New password'), required=False,
        help_text=_("This will change the user's password immediately, "
                    "leave blank to keep it as is!"))

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']

    def save(self, commit=True, set_password=True):
        user = super(UserAdminForm, self).save(commit=False)
        if set_password:
            user.set_password(self.cleaned_data['set_password'])
        if commit:
            user.save()
        return user


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    fieldsets = [
        (None, {'fields': ['email']}),
        (_('Password'), {'fields': ['password', 'set_password'], 'classes': ['collapse']}),
        (_('Permissions'), {'fields': ['is_active', 'is_superuser', 'groups', 'user_permissions']}),
        (_('Important dates'), {'fields': ['created', 'last_login']}),
    ]
    list_display = ['email', 'is_active', 'is_superuser']
    list_filter = ['is_active', 'is_superuser', 'groups']
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ['groups', 'user_permissions']
    readonly_fields = ['created', 'last_login']
