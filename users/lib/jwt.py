import jwt
import logging
from functools import wraps
from rest_framework.response import Response
from django.http import JsonResponse

from b2b_users.settings import JWT_SECRET_KEY

logger = logging.getLogger()


def token_required(f):
    @wraps(f)
    def decorated(self, request, *args, **kwargs):
        #token = request.META.get('HTTP_X_ACCESS_TOKEN')
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        if not token:
            logger.warning('token is MISSING:'+ str(request.META))
            return JsonResponse({'message': 'Token is missing!'}, status=401)

        try:
            data = jwt.decode(token, JWT_SECRET_KEY, leeway=60)
            logger.warning('token correct: ' + str(token) + ' data:' + str(data))
        except Exception as e:
            logger.warning('token is INVALID: ' + str(e))
            return JsonResponse({'message': 'Token %s is invalid! %s' % (token, str(e))}, status=401)

        return f(self, request, *args, **kwargs)

    return decorated
