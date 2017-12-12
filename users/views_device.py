# -*- coding: utf-8 -*-
# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist
import datetime

from .models import User, Device
from .serializers import TrackSerializer, DeviceSerializer
from .lib import gen_client_key


class DeviceLogin(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        user = User.objects.get(email=request.data['em'])
        if user.password != request.data['pwd']:
            return Response({'scs': False, 'emsg': 4}, status.HTTP_401_UNAUTHORIZED)
        device = {
            'user': user.id,
            'client_key': gen_client_key(),
            'token': request.data['token'],
            'model': request.data['man']+' '+request.data['mod'],
            'is_ios': False,
            'os_version': request.data['osv']
        }
        serializer = DeviceSerializer(data=device)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        try:
            # Удаляем старое устройство
            Device.objects.filter(user=user).delete()
            # Сохраняем новое
            serializer.save()
        except IntegrityError as e:
            return Response({'detail': str(e)}, status.HTTP_409_CONFLICT)
        # Формируем ответ
        res = {
            'cid': serializer.data['id'],
            'ckey': serializer.data['client_key']
        }
        return Response({'scs': True, 'res': res}, status.HTTP_200_OK)


class DeviceUpdate(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            device = Device.objects.get(pk=int(request.data['cid']), client_key=request.data['ckey'])
        except ObjectDoesNotExist:
            return Response({'scs': False, 'emsg': 16}, status=466)
        geo = {
            'user': device.user.id,
            'latitude': request.data['geo']['lat'],
            'longitude': request.data['geo']['long'],
            'date': datetime.datetime.now()
        }
        serializer = TrackSerializer(data=geo)
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError as e:
                return Response({'detail': str(e)}, status.HTTP_409_CONFLICT)
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class DeviceLogout(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            device = Device.objects.get(pk=int(request.data['cid']), client_key=request.data['ckey'])
        except ObjectDoesNotExist:
            return Response({'scs': False, 'emsg': 16}, status=466)
        if device.client_key == request.data['ckey'] and device.user.password == request.data['pwd']:
            device.delete()
            return Response({'scs': True})
        else:
            return Response({'scs': False, 'emsg': 4}, status.HTTP_401_UNAUTHORIZED)


class DummyView(APIView):

    def post(self, request, **kwargs):
        return Response({'scs': True})
