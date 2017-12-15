# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist


from users.models import User, Group, Role, Department, Track
from users.serializers.users import UserSerializer, UserListSerializer
from users.serializers.users import GroupSerializer, GroupListSerializer
from users.serializers.users import RoleSerializer
from users.serializers.users import DepartmentSerializer
from users.serializers.users import TrackListSerializer
from users.lib.generate_password import generate_password
from users.lib.queue_notice import queue_notice
from .abstract_view import AbstractList, get_object


class DepartmentsList(AbstractList):

    def __init__(self):
        super().__init__(Department, DepartmentSerializer)
