# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from ..views import HomeView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomeView.as_view(), name='home'),
    # url(r'^myApp/', include('apps.myapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    ) + urlpatterns
