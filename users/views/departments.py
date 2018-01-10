# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer

from users.models import Department
from users.serializers.departments import DepartmentSerializer


class DepartmentsList(generics.ListCreateAPIView):
    """
    get:
    Возвращает список подразделений

    post:
    Создает новое подразделение
    """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)


class DepartmentsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Просмотр подразделения

    put:
    Измение подразделения

    patch:
    Частичное измение подразделения

    delete:
    Удаление подразделения
    """
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = (AllowAny,)
    renderer_classes = (JSONRenderer,)
