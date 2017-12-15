# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import groups

# b2b/groups/
urlpatterns = [
    url(r'^$', groups.GroupsList.as_view(), name='groups-list'),
    url(r'^(?P<pk>\d+)/$', groups.GroupsDetail.as_view(), name='groups-detail'),
]
