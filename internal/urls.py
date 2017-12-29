# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^push/$', views.PushDevice.as_view(), name='push-device'),
]
