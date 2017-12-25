# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Track, Device, Profile


class TrackSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Track
        fields = ('id', 'user', 'date', 'latitude', 'longitude',)
        read_only_fields = ('id',)


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Device
        fields = ('id', 'user', 'client_key', 'token', 'model', 'is_ios', 'os_version',)
        read_only_fields = ('id',)


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    body = serializers.JSONField()

    class Meta:
        model = Profile
        fields = ('id', 'name', 'body')
