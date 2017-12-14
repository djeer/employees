# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import User, Group, Role, Department, Track, Device


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'name',)


class GroupListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'name', 'count')

    def get_count(self, obj):
        return obj.users.count()


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Role
        fields = ('id', 'name',)


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Department
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id',  'email', 'phone', 'password',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'department_id', 'job_title',
                  'group_id', 'role_id', 'is_ldap',
                  'ldap_login',)
        read_only_fields = ('id', 'device')
        extra_kwargs = {'password': {'write_only': True}}


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    device = serializers.SlugRelatedField(read_only=True, slug_field='model')

    class Meta:
        model = User
        fields = ('id', 'email', 'phone', 'password',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'department_id', 'job_title',
                  'group_id', 'role_id', 'is_ldap',
                  'device',)
        read_only_fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}


class TrackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('user_id', 'date', 'latitude', 'longitude',)


class DeviceSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Device
        fields = ('id', 'user', 'client_key', 'token', 'model', 'is_ios', 'os_version',)
        read_only_fields = ('id',)
