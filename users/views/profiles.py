# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import Profile
from users.serializers.profiles import ProfileSerializer, ProfileListSerializer


class ProfileList(generics.ListCreateAPIView):
    """
    get:
    Возвращает список профилей настроек

    post:
    Создает новый профиль настроек
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = (AllowAny,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Просмотр профиля

    put:
    Измение профиля

    patch:
    Частичное измение профиля

    delete:
    Удаление профиля
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
