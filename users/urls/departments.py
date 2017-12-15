# -*- coding: utf-8 -*-
from django.conf.urls import url
from users.views import departments

# b2b/departments/
urlpatterns = [
    url(r'^$', departments.DepartmentsList.as_view(), name='departments-list'),
]
