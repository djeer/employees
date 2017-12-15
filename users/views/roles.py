# -*- coding: utf-8 -*-
# Create your views here.

from users.models import User, Group, Role, Department, Track
from users.serializers.users import RoleSerializer
from .abstract_view import AbstractList, AbstractDetail


class RolesList(AbstractList):

    def __init__(self):
        super().__init__(Role, RoleSerializer)


class RolesDetail(AbstractDetail):

    def __init__(self):
        super().__init__(Role, RoleSerializer)