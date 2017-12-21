# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    body = serializers.JSONField()

    class Meta:
        model = Profile
        fields = ('id', 'name', 'body')


class ProfileListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Profile
        fields = ('id', 'name')
