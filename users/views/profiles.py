# -*- coding: utf-8 -*-
# Create your views here.

from users.models import Profile
from users.serializers.profiles import ProfileSerializer, ProfileListSerializer
from .abstract_view import AbstractList, AbstractDetail


class ProfileList(AbstractList):

    def __init__(self):
        super().__init__(Profile, ProfileListSerializer)


class ProfileDetail(AbstractDetail):

    def __init__(self):
        super().__init__(Profile, ProfileSerializer)
