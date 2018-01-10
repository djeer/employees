# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import Role
from users.serializers.roles import RoleSerializer


class RolesList(generics.ListCreateAPIView):
    """
    get:
    Возвращает список ролей пользователей

    post:
    Создает новую роль
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (AllowAny,)


class RolesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Просмотр роли

    put:
    Измение роли

    patch:
    Частичное измение роли

    delete:
    Удаление роли
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (AllowAny,)
