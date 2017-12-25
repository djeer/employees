# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.db import models
from users.models import User, Group, Role


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    group_id = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), source='group', required=False)
    role_id = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), source='role', required=False)

    class Meta:
        model = User
        fields = ('id',  'email', 'phone', 'password',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'department_id', 'job_title',
                  'group_id', 'role_id',
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
                  'group_id', 'role_id',
                  'device',)
        read_only_fields = ('id', 'device',)
        extra_kwargs = {'password': {'write_only': True}}


class UserExcelSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id',  'email', 'phone',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'job_title',)
        read_only_fields = ('id',)
