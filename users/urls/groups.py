# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import users

# b2b/users/
urlpatterns = [
    url(r'^$', users.GroupsList.as_view(), name='groups-list'),
]
