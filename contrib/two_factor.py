# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from two_factor import views


class DisableView(views.DisableView):
    """
    Override `redirect_url`.

    """
    redirect_url = reverse_lazy('accounts:detail')
