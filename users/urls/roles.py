# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import users

# b2b/roles/
urlpatterns = [
    url(r'^$', users.RolesList.as_view(), name='roles-list'),
]
