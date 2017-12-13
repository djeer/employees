# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import devices

urlpatterns = [
    url(r'^login/$', devices.DeviceLogin.as_view(), name='device-login'),
    url(r'^update/$', devices.DeviceUpdate.as_view(), name='device-update'),
    url(r'^apps/$', devices.DummyView.as_view(), name='device-update'),
    url(r'^token/$', devices.DummyView.as_view(), name='device-token'),
    url(r'^batch/$', devices.DummyView.as_view(), name='device-batch'),
    url(r'^logout/$', devices.DeviceLogout.as_view(), name='device-logout'),
]
