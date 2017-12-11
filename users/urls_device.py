# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views_device

urlpatterns = [
    url(r'^login/$',  views_device.DeviceLogin,  name='device-login'),
    url(r'^update/$', views_device.DeviceUpdate, name='device-update'),
    url(r'^logout/$', views_device.DeviceLogout, name='device-logout'),
]
