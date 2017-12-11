# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.UsersList.as_view(), name='users-list'),
    url(r'^users/(?P<pk>\d+)/$', views.UsersDetail.as_view(), name='users-detail'),
    url(r'^groups/$', views.GroupsList.as_view(), name='groups-list'),
    url(r'^users/(?P<pk>\d+)/track/$', views.TrackDetail.as_view(), name='track-detail'),
]
