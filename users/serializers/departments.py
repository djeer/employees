# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Department
        fields = ('id', 'name',)
