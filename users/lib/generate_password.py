import random
import string
from .queue_notice import queue_notice


def generate_password():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(10))
