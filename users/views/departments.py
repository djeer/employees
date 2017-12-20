# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist


from users.models import Department
from users.serializers.departments import DepartmentSerializer
from .abstract_view import AbstractList, AbstractDetail


class DepartmentsList(AbstractList):

    def __init__(self):
        super().__init__(Department, DepartmentSerializer)


class DepartmentsDetail(AbstractDetail):

    def __init__(self):
        super().__init__(Department, DepartmentSerializer)
