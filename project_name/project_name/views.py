# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomeView(TemplateView):
    """The index page."""

    template_name = 'index.html'
