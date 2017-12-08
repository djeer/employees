# -*- coding: utf-8 -*-
from django.db import models


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    ldap_login = models.TextField(max_length=256, unique=True)
    password = models.TextField(max_length=64, null=True)
    email = models.EmailField(max_length=256, unique=True)
    phone = models.TextField(max_length=20, unique=True)

    first_name = models.TextField(max_length=256)
    middle_name = models.TextField(max_length=256)
    last_name = models.TextField(max_length=256)
    office = models.TextField(max_length=256)
    dept = models.TextField(max_length=256)
    image_uuid = models.TextField(max_length=36)

    group_id = models.ForeignKey(Group, related_name='users', default=None, on_delete=models.SET_DEFAULT, null=True)

    is_ldap = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
