# -*- coding: utf-8 -*-
from django.conf.urls import url
from devices import views

urlpatterns = [
    url(r'^login/$', views.DeviceLogin.as_view(), name='device-login'),
    url(r'^update/$', views.DeviceUpdate.as_view(), name='device-update'),  # old
    url(r'^geo/$', views.DeviceUpdate.as_view(), name='device-geo'),
    url(r'^status/$', views.DeviceUpdateStatus.as_view(), name='device-status'),
    url(r'^profile/$', views.DeviceProfile.as_view(), name='device-profile'),
    url(r'^apps/$', views.DummyView.as_view()),
    url(r'^token/$', views.DummyView.as_view()),
    url(r'^batch/$', views.DummyView.as_view()),
    url(r'^logout/$', views.DeviceLogout.as_view(), name='device-logout'),
]
