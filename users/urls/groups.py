# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import groups

# b2b/users/
urlpatterns = [
    url(r'^$', groups.GroupsList.as_view(), name='groups-list'),
]
