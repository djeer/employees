# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Group, Profile


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    count = serializers.SerializerMethodField()
    profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), source='profile', required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'profile_id', 'count')
        read_only_fields = ('count',)

    def get_count(self, obj):
        return obj.users.count()


class GroupListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    count = serializers.SerializerMethodField()
    profile_id = serializers.PrimaryKeyRelatedField(queryset=Profile.objects.all(), source='profile', required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'profile_id', 'count')
        read_only_fields = ('count',)

    def get_count(self, obj):
        return obj.users.count()

