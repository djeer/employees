# -*- coding: utf-8 -*-
# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import Profile
from users.serializers.profiles import ProfileSerializer, ProfileListSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileListSerializer
    permission_classes = (AllowAny,)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (AllowAny,)
