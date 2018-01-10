# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import Group
from users.serializers.groups import GroupSerializer, GroupListSerializer


class GroupsList(generics.ListCreateAPIView):
    """
    get:
    Возвращает список групп пользователей

    post:
    Создает новую группу пользователей
    """
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = (AllowAny,)


class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Просмотр группы

    put:
    Измение группы

    patch:
    Частичное измение группы

    delete:
    Удаление группы
    """
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (AllowAny,)
