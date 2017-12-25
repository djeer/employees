# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import users

# b2b/users/
urlpatterns = [
    url(r'^$', users.UsersList.as_view(), name='users-list'),
    url(r'^(?P<pk>\d+)/$', users.UsersDetail.as_view(), name='users-detail'),
    url(r'^(?P<pk>\d+)/track/$', users.TrackList.as_view(), name='track-list'),
    url(r'^(?P<pk>\d+)/device/$', users.DeviceDetail.as_view(), name='device-detail'),
    url(r'^geo/$', users.TrackRecentUpdate.as_view(), name='track-last-update'),
    url(r'^excel/$', users.UsersExcel.as_view(), name='excel'),
]
