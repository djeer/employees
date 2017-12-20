# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import User


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
