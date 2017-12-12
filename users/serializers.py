# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import User, Group, Track, Device


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id', 'ldap_login', 'email', 'phone',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'dept', 'group_id',)
        read_only_fields = ('id',)


class TrackSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Track
        fields = ('id', 'user_id', 'date', 'latitude', 'longitude',)
        read_only_fields = ('id',)


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Device
        fields = ('id', 'user_id', 'client_key', 'token', 'model', 'is_ios', 'os_version',)
        read_only_fields = ('id',)

