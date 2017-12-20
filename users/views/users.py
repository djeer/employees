# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist


from users.models import User, Group, Role, Department, Track, Device
from users.serializers.users import UserSerializer, UserListSerializer
from users.serializers.users import DeviceDetailSerializer
from users.serializers.users import TrackListSerializer
from users.lib.generate_password import generate_password
from users.lib.queue_notice import queue_notice
from .abstract_view import AbstractList, get_object


class UsersList(APIView):

    def __init__(self):
        super().__init__()
        self.filter_str_fields = ('first_name', 'middle_name', 'last_name', 'dept', 'job_title', 'email', 'phone', )
        self.filter_int_fields = ('group_id', 'role_id', 'group', 'role')

    def get(self, request, **kwargs):
        # получаем query params
        try:
            start = int(request.query_params.get('start', 0))
            limit = int(request.query_params.get('limit', 10))
            order_field = request.query_params.get('sortf')            # поля для фильтров
            qs_filter = {}
            # поля integer - поиск только полного совпадения
            for k in self.filter_int_fields:
                if k in request.query_params:
                    qs_filter[k] = int(request.query_params.get(k))
            # строковые поля - поиск вхождений через ILIKE
            for k in self.filter_str_fields:
                if k in request.query_params:
                    qs_filter['%s__icontains' % k] = request.query_params.get(k)
        except Exception as e:
            return Response({'detail': 'Wrong query params: %s' % str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # поле для сортировки по-умолчанию
        if not order_field:
            order_field = 'last_name'

        # переворот сортировки
        if request.query_params.get('sortt') == '1':
            order_field = '-'+order_field

        # выбираем пользователей с фильтром (распаковываем словарь как аргументы kwargs)
        query_set = User.objects.filter(**qs_filter)
        count = query_set.count()

        # сортируем и обрезаем
        query_set = query_set.order_by(order_field)[start:start+limit]

        serializer = UserListSerializer(query_set, many=True)
        response = {
            'users': serializer.data,
            'users_count': count,
            'qs_filter': qs_filter
        }
        return Response(response, status=status.HTTP_200_OK)

    def post(self, request, **kwargs):
        request.data['password'] = generate_password()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status=status.HTTP_409_CONFLICT)
            notice = {
                "mail": serializer.data['email'],
                "subj": "Ваш новый пароль 2bsafe",
                "text": "Ваш новый пароль 2bsafe: %s" % request.data['password']
            }
            queue_notice(notice, 'email')
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


class DeviceDetail(APIView):

    def get(self, request, pk, **kwargs):
        device = Device.objects.get(user_id=pk)
        serializer = DeviceDetailSerializer(device)
        return Response(serializer.data, status=status.HTTP_200_OK)


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
