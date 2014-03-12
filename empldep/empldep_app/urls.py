from django.conf.urls import patterns, include, url
from .views import users_json, user_json

urlpatterns = patterns('',
                       url(r'^get_users/$', users_json),
                       url(r'^get_user/(?P<id>\d+)$', user_json),
                       )
