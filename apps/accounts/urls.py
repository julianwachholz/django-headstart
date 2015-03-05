# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.detail, name='detail'),
    url(r'^password/$', views.password_change, name='password_change'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.create, name='create'),
]
