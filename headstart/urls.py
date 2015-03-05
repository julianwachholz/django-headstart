# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin
from two_factor.urls import core as two_factor_patterns
from two_factor.views import ProfileView

from contrib.two_factor import DisableView
from .views import IndexView


two_factor_profile = [
    url(r'^account/two_factor/$', ProfileView.as_view(), name='profile'),
    url(r'^account/two_factor/disable/$', DisableView.as_view(), name='disable'),
]

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^account/', include('apps.accounts.urls', namespace='accounts')),
    url(r'', include(two_factor_patterns + two_factor_profile, namespace='two_factor')),
    url(r'^admin/', include(admin.site.urls)),
]
