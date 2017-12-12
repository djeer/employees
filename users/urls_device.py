# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views_device

urlpatterns = [
    url(r'^login/$',  views_device.DeviceLogin.as_view(),  name='device-login'),
    url(r'^update/$', views_device.DeviceUpdate.as_view(), name='device-update'),
    url(r'^apps/$', views_device.DummyView.as_view(), name='device-update'),
    url(r'^token/$', views_device.DummyView.as_view(), name='device-update'),
    url(r'^logout/$', views_device.DeviceLogout.as_view(), name='device-logout'),
]
