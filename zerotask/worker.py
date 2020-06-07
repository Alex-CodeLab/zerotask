import ast
import json
import os
import signal
import sys
import zmq
from tasks import *

context = zmq.Context()
receiver = context.socket(zmq.PULL)
receiver.bind('tcp://127.0.0.1:5588')

# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://127.0.0.1:5589")

# todo: clean kill- wait until all processes are finished
def signal_handler(signum, frame):
    signal.signal(signum, signal.SIG_IGN) # ignore additional signals
    sys.exit(0)


if __name__ == '__main__':

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        msg = receiver.recv()
        queue, tid, func, arg, kwarg = msg.split(b' ', maxsplit=4)
        arg= tuple(arg.decode().split(','))
        kwargs= ast.literal_eval(kwarg.decode())
        sender.send(tid+ b' 1') # status running
        result = getattr(Tasks, func.decode())(*arg, **kwargs)
        sender.send(tid + b' 2') # status completed
