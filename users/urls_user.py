# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views_user, views_device

# b2b/users/
urlpatterns = [
    url(r'^$', views_user.UsersList.as_view(), name='users-list'),
    url(r'^(?P<pk>\d+)/$', views_user.UsersDetail.as_view(), name='users-detail'),
    url(r'^groups/$', views_user.GroupsList.as_view(), name='groups-list'),
    url(r'^(?P<pk>\d+)/track/$', views_user.TrackList.as_view(), name='track-list'),
    url(r'^(?P<pk>\d+)/geo/$', views_user.TrackRecentUpdate.as_view(), name='track-last-update'),
]
