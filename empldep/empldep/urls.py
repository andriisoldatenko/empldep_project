from django.conf.urls import patterns, include, url
from django.contrib import admin
from empldep_app.views import users_json
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('empldep_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
