from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import IndexView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view(), name='index'),
    #url(r'^accounts/', include('apps.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
