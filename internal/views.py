# -*- coding: utf-8 -*-
# Create your views here.

import logging
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.db import IntegrityError
from django.db.models import ObjectDoesNotExist
import datetime

from users.lib.queue_notice import queue_notice
from users.models import Device

logger = logging.getLogger()


class PushDevice(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        try:
            device_id = request.data['device_id']
            body = request.data['body']
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        token = Device.objects.get(pk=device_id).token
        # отправляем пуш на клиента
        notice = {
            "token": token,
            "data": body
        }
        queue_notice(json.dumps(notice), 'push')

        return Response(status=status.HTTP_204_NO_CONTENT)
