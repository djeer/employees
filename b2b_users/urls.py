"""b2b_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Users API')

urlpatterns = [
    # Docs
    url(r'^b2b/users/docs/$', schema_view),
    url(r'^b2b/users/docs2/', include_docs_urls(title='My API title')),
    # Admin
    url(r'^b2b/admin/users/', admin.site.urls),
    # WEB:
    url(r'^b2b/departments/', include('users.urls.departments')),
    url(r'^b2b/groups/', include('users.urls.groups')),
    url(r'^b2b/roles/', include('users.urls.roles')),
    url(r'^b2b/users/', include('users.urls.users')),
    url(r'^b2b/profiles/', include('users.urls.profiles')),
    # Android client API
    url(r'^b2b/devices/', include('devices.urls')),
    # Internal API TODO: rewrite
    url(r'^b2b/devices/internal/', include('internal.urls')),
]
