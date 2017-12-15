# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import roles

# b2b/roles/
urlpatterns = [
    url(r'^$', roles.RolesList.as_view(), name='roles-list'),
    url(r'^(?P<pk>\d+)/$', roles.RolesDetail.as_view(), name='roles-detail'),
]
