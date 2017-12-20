# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Group


class GroupSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'name', 'count')

    def get_count(self, obj):
        return obj.users.count()


class GroupListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    count = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ('id', 'name', 'count')
        read_only_fields = ('count',)

    def get_count(self, obj):
        return obj.users.count()

