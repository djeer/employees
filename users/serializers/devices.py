# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Device


class DeviceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = ('signal', 'battery',)
