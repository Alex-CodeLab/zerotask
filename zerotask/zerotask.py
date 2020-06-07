import uuid
import threading
import zmq
import sys
from functools import partial, wraps
from .models import Task

ctx = zmq.Context()
ctx.IPV6 = False
# terminates context instead of hang forever when an
# unexpected exception occurs
ctx.LINGER = 300


sender = ctx.socket(zmq.PUSH)
sender.connect('tcp://127.0.0.1:5588')

def collect():
    """ collects returned messaged and updates db
    """
    receiver = ctx.socket(zmq.PULL)
    receiver.bind('tcp://127.0.0.1:5589')
    print('collector started')
    while True:
        msg = receiver.recv()
        tid, status = msg.split(b' ')
        if status == b'1':
            Task.objects.filter(tid=tid.decode()).update(status=1)
        if status == b'2':
            Task.objects.filter(tid=tid.decode()).update(status=2)

if 'runserver' in sys.argv:
    threading.Thread(target=collect).start()


# decorator optional argument
# https://stackoverflow.com/questions/653368/how-to-create-a-python-decorator-that-can-be-used-either-with-or-without-paramet
def task(func=None, queue=0):
    if func is None:
        return partial(task, queue=queue)

    @wraps(func)
    def wrapper(*args, **kwargs):
        args = ','.join(map(str, args))
        tid = uuid.uuid4().hex
        msg = '{} {} {} {} {}'.format(
            queue, tid, func.__name__, args, kwargs)
        Task.objects.create(queue=queue, tid=tid, msg=msg)
        sender.send_string(msg)
    return wrapper
