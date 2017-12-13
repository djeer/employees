# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import users

# b2b/users/
urlpatterns = [
    url(r'^$', users.UsersList.as_view(), name='users-list'),
    url(r'^(?P<pk>\d+)/$', users.UsersDetail.as_view(), name='users-detail'),
    url(r'^groups/$', users.GroupsList.as_view(), name='groups-list'),
    url(r'^(?P<pk>\d+)/track/$', users.TrackList.as_view(), name='track-list'),
    url(r'^geo/$', users.TrackRecentUpdate.as_view(), name='track-last-update'),
]
