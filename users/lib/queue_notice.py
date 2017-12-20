#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kombu import Connection
import json
import requests


def queue_notice(j_string, type, urgent=False):
    return queue_notice_post(j_string, type, urgent=urgent)


def queue_notice_post(j_string, type, urgent=False):
    """Получает сообщение json и закидывает его POST запросом в b2c сервис
       (это нужно, чтобы работать с другого сервера без доступа к RabbitMQ
       потому что админа хер допросишься пробросить порты)
       Формат сообщений:
    {
        "phone":"798811122233", #обязательно для sms
        "mail":"vasya@mail.ru", #обязательно для email
        "subj":"MDM Notice",    #обязательно для email
        "token":"QWERTY12345"   #обязательно для push
        "data": {}              #обязательно для push
        "text":"You've just been erased" #текст, для всех видов, кроме пуш
    }
    """
    url = 'https://api.safec.ru/s_mdm/lib/queue_notice'
    r = requests.post(url, json={"j_string": j_string, "type": type, "urgent": urgent}, timeout=10)


def queue_notice_rmq(j_string, type, urgent=False):
    """Получает сообщение json и закидывает его в необходимую очередь rabbitmq
        Формат сообщений:
    {
        "phone":"798811122233", #обязательно для sms
        "mail":"vasya@mail.ru", #обязательно для email
        "subj":"MDM Notice",    #обязательно для email
        "token":"QWERTY12345"   #обязательно для push
        "data": {}              #обязательно для push
        "text":"You've just been erased" #текст, для всех видов, кроме пуш
    }
    """
    #with Connection('amqp://guest:guest@localhost:5672//') as conn:
    with Connection('amqp://safecom:safe-com-140@vm0:5672//') as conn:
        #выбираем очередь
        #if (type == 'sms' and urgent):
        #    rmq = conn.SimpleQueue('sms_fast')
        #elif (type =='sms'):
        #    rmq = conn.SimpleQueue('sms_slow')
        if (type == 'sms' and urgent):
            rmq = conn.SimpleQueue('sms_alma')
        elif (type =='sms'):
            rmq = conn.SimpleQueue('sms_alma')

        elif (type =='email'):
            rmq = conn.SimpleQueue('email')
        elif (type =='email_support'):
            rmq = conn.SimpleQueue('email_support')
        elif (type =='push_lk'):
            rmq = conn.SimpleQueue('push_lk')
        elif (type =='push'):
            rmq = conn.SimpleQueue('push_fast')
        elif (type =='socketio'):
            rmq = conn.SimpleBuffer('socketio_buffer')
        else:
            raise IndexError('Wrong notice type!')
        #засовываем полученный json в очередь
        rmq.put(j_string)
        print(('Sent: %s' % j_string))
        rmq.close()

#if __name__ == '__main__':
#    msg = {
#        "token": "dDnuR4-WmNU:APA91bEjvu5NsbBUdxd9Rl9I7Db6oBQUn7TMk94JE9n-yQ2dFpLgflFk4C-WxYnSjI-Uq5qkRFzsDAQx9S-dDNzhUHwHNzXI0pmTQ19VQ-ZlI7Ddaf0_2TlxqfrhVMSYLqVjNZ_NlDpF",
#        "data": {"action":1}
#    }
#    queue_notice(json.dumps(msg), 'push')
