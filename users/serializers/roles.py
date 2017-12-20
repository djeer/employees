# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Role


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Role
        fields = ('id', 'name',)