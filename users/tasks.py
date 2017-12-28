# -*- coding: utf-8 -*-
import enum
import queue
import logging

from django.db import models
from singleton_decorator import singleton
import requests

logger = logging.getLogger()

TASKS_URL = "https://lkn.safec.ru/b2b/tasks/internal/queue/"


class TaskType(enum.Enum):
    PUSH_PROFILE = 'push_profile'
    DISCONNECT_DEVICE = 'disconnect_device'


class Task:

    def __init__(self, user, task_type: TaskType):
        self.user = user
        self.type = task_type

    def get_name(self):
        if self.type == TaskType.PUSH_PROFILE:
            return "Смена роли"
        elif self.type == TaskType.DISCONNECT_DEVICE:
            return "Отключить устройство"
        else:
            raise ValueError('unknown task type: %s' % str(self.type))

    def get_detail(self):
        return self.get_name()


#@singleton
class TaskQueue:
    def __init__(self):
        self.tasks = queue.Queue()

    def add(self, task: Task):
        self.tasks.put(task)

    def push_all(self):
        while not self.tasks.empty():
            task = self.tasks.get()
            self.push_one(task)

    @staticmethod
    def push_one(task: Task):
        try:
            device_name = task.user.device.model
        except models.ObjectDoesNotExist:
            logger.warning('device is not connected')
            return

        task_name = task.get_name()
        task_detail = task.get_detail()
        task_data = {
            "user_id": task.user.id,
            "user_name": f"{task.user.last_name} {task.user.first_name} {task.user.middle_name}",
            "user_group": task.user.group.name,
            "name": task_name,
            "description": task_detail,
            "device_name": device_name
        }
        try:
            r = requests.post(TASKS_URL, json=task_data)
            if r.status_code != 201:
                raise IOError(f"response code: {str(r.status_code)}, body: {str(r.text)}")
            logger.warning('pushed task %s' % str(task_data))
        except Exception as e:
            raise IOError("Can't add task: %s because of: %s" % (str(task_data), str(e)))

