# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    ldap_login = models.TextField(max_length=256, unique=True, null=True)
    password = models.TextField(max_length=64, null=True)
    email = models.EmailField(max_length=256, unique=True)
    phone = models.TextField(max_length=20, unique=True)

    first_name = models.TextField(max_length=256)
    middle_name = models.TextField(max_length=256)
    last_name = models.TextField(max_length=256)
    office = models.TextField(max_length=256)
    dept = models.TextField(max_length=256)
    job_title = models.TextField(max_length=256)
    image_uuid = models.TextField(max_length=36)

    group_id = models.ForeignKey(Group, related_name='users', default=None, on_delete=models.SET_DEFAULT, null=True)
    role = models.ForeignKey(Role, related_name='users', default=None, on_delete=models.SET_DEFAULT, null=True)

    is_ldap = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id+' '+self.email)


class Track(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='track', on_delete=models.CASCADE)
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()


class Device(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, related_name='device', on_delete=models.CASCADE)
    client_key = models.TextField(null=False)
    login_date = models.DateTimeField(null=False, default=now)
    token = models.TextField()
    model = models.TextField()
    is_ios = models.BooleanField()
    os_version = models.TextField()

    def __str__(self):
        return str('My Device Model')
