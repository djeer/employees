# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import profiles

# b2b/profiles/
urlpatterns = [
    url(r'^$', profiles.ProfileList.as_view(), name='profiles-list'),
    url(r'^(?P<pk>\d+)/$', profiles.ProfileDetail.as_view(), name='profiles-detail'),
]
