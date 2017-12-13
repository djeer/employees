# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.db.models import ObjectDoesNotExist
import datetime

from .models import User, Group, Track
from .serializers_user import UserSerializer, UserListSerializer
from .serializers_user import GroupSerializer, GroupListSerializer
from .serializers_user import TrackListSerializer


def get_object(model, pk):
    try:
        return model.objects.get(pk=pk)
    except model.DoesNotExist:
        raise NotFound


class GroupsList(APIView):

    def get(self, request, **kwargs):
        groups = Group.objects.all()
        serializer = GroupListSerializer(groups, many=True)
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

    def __init__(self):
        super(UsersList, self).__init__()
        self.filter_fields = model_to_dict(User).keys()

    def get(self, request, **kwargs):
        count = User.objects.count()
        # получаем query params
        try:
            start = int(request.query_params['start'])
            limit = int(request.query_params['limit'])
            order_field = request.query_params['sortf']
            # Поля для фильтров
            qs_filter = {}
            for k in self.filter_fields:
                if k in request.query_params:
                    qs_filter[k] = request.query_params.get(k)
        except Exception as e:
            return Response({'detail': 'Wrong query params: %s' % str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # поле для сортировки
        if not order_field:
            order_field = 'last_name'

        # переворот сортировки
        if request.query_params.get('sortt') == '1':
            order_field = '-'+order_field

        # выбираем пользователей с фильтром
        query_set = User.objects.all().filter(**qs_filter)

        # сортируем и обрезаем
        query_set = query_set.order_by(order_field)[start:limit]

        serializer = UserListSerializer(query_set, many=True)
        response = {
            'users': serializer.data,
            'users_count': count,
            'qs_filter': qs_filter
        }
        return Response(response, status=status.HTTP_200_OK)

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

    def patch(self, request, pk, **kwargs):
        user = get_object(User, pk)
        if 'group_id' in request.data:
            request.data['group_id'] = get_object(Group, request.data['group_id'])

        serializer = UserSerializer()
        if serializer.update(user, request.data):
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        user = get_object(User, pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TrackList(APIView):

    def get(self, request, pk, **kwargs):
        points = Track.objects.filter(user_id=pk).order_by('date')
        serializer = TrackListSerializer(points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TrackRecentUpdate(APIView):

    def get(self, request, **kwargs):
        users = request.query_params.get('id').split(',')
        users = [int(x) for x in users]

        points = []
        for i in users:
            try:
                points.append(Track.objects.filter(user_id=i).latest('date'))
            except ObjectDoesNotExist:
                pass
        serializer = TrackListSerializer(points, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
