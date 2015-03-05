# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required

from vanilla import DetailView, CreateView, FormView

from .forms import UserCreateForm, PasswordChangeForm
from .models import User


def logout(request):
    auth.logout(request)
    messages.info(request, _('You have been logged out.'))
    return redirect('index')


class PasswordMixin(object):
    """
    Keep the session logged in after setting a user's password.

    """
    def get_success_message(self):
        if not self.success_message:
            raise NotImplementedError('Implement get_success_message()')
        return self.success_message

    def form_valid(self, form):
        form.save()
        user = auth.authenticate(username=form.user.email,
                                 password=form.cleaned_data['password'])

        if user is None:
            messages.error(request, _('Authentication failed!'))
            return redirect('accounts:login')

        messages.success(self.request, self.get_success_message())
        auth.login(self.request, user)
        return redirect('accounts:detail')


class UserCreateView(PasswordMixin, CreateView):
    """
    This view will attempt to create a new user.

    If email verification is active, no user will be created.
    Instead, a signed link will be sent via email; clicking
    this link will automatically create a verified user account.

    """
    model = User
    form_class = UserCreateForm
    template_name_suffix = '_register'

    success_message = _('Thank you for registering!')

create = UserCreateView.as_view()


class UserDetailView(DetailView):
    """
    View your account details.

    """
    name = 'user_detail'
    model = User

    def get_object(self):
        return self.request.user

detail = login_required(UserDetailView.as_view())


class PasswordChangeView(PasswordMixin, FormView):
    """
    Let users change their password.

    """
    name = 'password_change'
    form_class = PasswordChangeForm
    template_name = 'accounts/change_password.html'

    success_message = _('Password changed!')

    def get_form(self, *args, **kwargs):
        kwargs.update({'user': self.request.user})
        return super(PasswordChangeView, self).get_form(*args, **kwargs)

password_change = login_required(PasswordChangeView.as_view())
