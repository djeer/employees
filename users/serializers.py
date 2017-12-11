# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import User, Group


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('id', 'ldap_login', 'email', 'phone',
                  'first_name', 'middle_name', 'last_name',
                  'office', 'dept', 'group_id',)
        read_only_fields = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Group
        fields = ('id', 'name',)
