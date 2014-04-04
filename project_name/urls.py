from django.conf.urls import include, url
from django.contrib import admin

from .views import IndexView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    #url(r'^accounts/', include('apps.accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
