# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now
from jsonfield import JSONField
import logging

from users.tasks import Task, TaskActions, TaskQueue

logger = logging.getLogger()


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    body = JSONField()


class Group(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)
    profile = models.ForeignKey(Profile, related_name='groups', on_delete=models.SET_DEFAULT, default=None, null=True)

    def __str__(self):
        return str(self.name)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)


class User(models.Model):

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.old_group_id = self.group_id

    id = models.BigAutoField(primary_key=True)
    ldap_login = models.TextField(max_length=256, unique=True, null=True)
    password = models.TextField(max_length=64, null=True)
    email = models.EmailField(max_length=256, unique=True)
    phone = models.TextField(max_length=20, unique=True)

    first_name = models.TextField(max_length=256, null=False)
    middle_name = models.TextField(max_length=256, blank=True, null=False, default='')
    last_name = models.TextField(max_length=256, null=False)
    office = models.TextField(max_length=256, blank=True, null=False, default='')
    job_title = models.TextField(max_length=256, blank=True, null=False, default='')
    image_uuid = models.TextField(max_length=36, null=True)

    group = models.ForeignKey(Group, related_name='users', default=0, on_delete=models.SET_DEFAULT, null=False)
    role = models.ForeignKey(Role, related_name='users', default=0, on_delete=models.SET_DEFAULT, null=False)
    department = models.ForeignKey(Department, related_name='users', default=0, on_delete=models.SET_DEFAULT, null=False)

    is_ldap = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+str(self.email)

    # переопределяем метод save, чтобы автоматически содзавать задачу на смену профиля
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        logger.warning(f"old group_id: {str(self.old_group_id)}, new group_id: {str(self.group_id)}")
        if self.old_group_id != self.group_id:
            task = Task(self, TaskActions.APPLY_PROFILE)
            TaskQueue.push_one(task)
        super(User, self).save(force_insert, force_update, using, update_fields)
        self.old_group_id = self.group_id


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
    # os
    is_ios = models.BooleanField()
    os_version = models.TextField()
    # status
    battery = models.IntegerField(null=True, default=None)
    signal = models.IntegerField(null=True, default=None)

    def __str__(self):
        return str(self.model)
