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


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound


class AbstractList(APIView):

    def __init__(self, model, serializer):
        super().__init__()
        self.model = model
        self.serializer = serializer

    def get(self, request, **kwargs):
        items = self.model.objects.all()
        serializer = self.serializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
