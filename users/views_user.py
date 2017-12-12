# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
import datetime

from .models import User, Group, Track
from .serializers import UserSerializer, GroupSerializer, TrackSerializer


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound


class GroupsList(APIView):

    def get(self, request, **kwargs):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersList(APIView):

    def get(self, request, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        request.data['password'] = 'qqqqqq'
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UsersDetail(APIView):

    def delete(self, request, pk, **kwargs):
        user = get_object(User, pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrackDetail(APIView):

    def get(self, request, pk, **kwargs):
        points = Track.objects.get(pk=pk)
        serializer = TrackSerializer(points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        serializer = TrackSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
