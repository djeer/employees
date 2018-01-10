# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import Group
from users.serializers.groups import GroupSerializer, GroupListSerializer


class GroupsList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    permission_classes = (AllowAny,)


class GroupsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (AllowAny,)
