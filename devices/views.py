# -*- coding: utf-8 -*-
# Create your views here.

import logging
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist
import datetime

from .models import User, Device
from .serializers import TrackSerializer, DeviceSerializer, ProfileSerializer
from .lib import gen_client_key

logger = logging.getLogger()


class DeviceLogin(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            user = User.objects.get(email=request.data['em'], password=request.data['pwd'])
        except ObjectDoesNotExist as e:
            return Response({'scs': False, 'emsg': 4}, status.HTTP_401_UNAUTHORIZED)

        # delete old device
        Device.objects.filter(user=user).delete()

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
            logger.warning(serializer.errors)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        try:
            # Сохраняем устройство
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


class DeviceUpdateStatus(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            device = Device.objects.get(pk=int(request.data['cid']), client_key=request.data['ckey'])
        except ObjectDoesNotExist:
            return Response({'scs': False, 'emsg': 16}, status=466)

        try:
            device_status = {
                'battery': request.data['battery'],
                'signal': request.data['signal']
            }
        except Exception as e:
            return Response({'scs': False, 'emsg': 4, 'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DeviceSerializer()
        if serializer.update(device, device_status):
            return Response({'scs': True}, status=status.HTTP_200_OK)
        return Response({'scs': False, 'emsg': 4, 'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DeviceProfile(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            device = Device.objects.get(pk=int(request.data['cid']), client_key=request.data['ckey'])
        except ObjectDoesNotExist:
            return Response({'scs': False, 'emsg': 16}, status=466)

        profile = device.user.role.profile

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


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
