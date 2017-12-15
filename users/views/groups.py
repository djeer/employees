# -*- coding: utf-8 -*-
# Create your views here.

from users.models import User, Group, Role, Department, Track
from users.serializers.users import GroupSerializer, GroupListSerializer
from .abstract_view import AbstractList, AbstractDetail


class GroupsList(AbstractList):

    def __init__(self):
        super().__init__(Group, GroupListSerializer)


class GroupsDetail(AbstractDetail):

    def __init__(self):
        super().__init__(Group, GroupSerializer)
