# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Role, Profile


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), source='profile', required=False)

    class Meta:
        model = Role
        fields = ('id', 'name', 'profile_id')
