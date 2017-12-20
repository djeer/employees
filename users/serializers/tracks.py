# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Track


class TrackListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Track
        fields = ('user_id', 'date', 'latitude', 'longitude',)
