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


urlpatterns_web = [
    # WEB:
    url(r'^b2b/departments/', include('users.urls.departments')),
    url(r'^b2b/groups/', include('users.urls.groups')),
    url(r'^b2b/roles/', include('users.urls.roles')),
    url(r'^b2b/users/', include('users.urls.users')),
    url(r'^b2b/profiles/', include('users.urls.profiles')),
]

urlpatterns_devices = [
    # Android client API
    url(r'^b2b/devices/', include('devices.urls')),
]


docs_url_drf = include_docs_urls(title='Users API', patterns=urlpatterns_web, schema_url='https://lkn.safec.ru')
docs_url_swagger = get_swagger_view(title='Users API', patterns=urlpatterns_web)

urlpatterns_docs = [
    # Docs
    url(r'^b2b/users/docs/', docs_url_drf),
    url(r'^b2b/users/docs2/$', docs_url_swagger),
    url(r'^b2b/users/devices-docs2/$', get_swagger_view(title='Devices API', patterns=urlpatterns_devices)),
    url(r'^b2b/users/devices-docs/', include_docs_urls(title='Devices API', patterns=urlpatterns_devices)),
]

urlpatterns_admin = [
    # Admin
    url(r'^b2b/admin/users/', admin.site.urls),
    # Internal API TODO: rewrite url
    url(r'^b2b/devices/internal/', include('internal.urls')),
]

urlpatterns = list(urlpatterns_admin + urlpatterns_docs + urlpatterns_web + urlpatterns_devices)
