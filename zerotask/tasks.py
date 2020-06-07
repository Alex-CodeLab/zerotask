import time

from functools import partial, wraps

def task(func=None, queue=0):
    """ Dummy wrapper, which is only used when this files is accessed by the worker
        It gets overwritten when this file is accessed by the producer/ django application.
    """
    if func is None:
         return partial(task, queue=queue)

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

try:
    from .zerotask import task
except:
    pass

###################

class Tasks():
    """ Any function can be offloaded to the worker by using the @task decorator
        Note that when a function is called by the worker, the arguments are
        parsed as string.
        Default queue = 0 , to set different queue: @task(queue=6)
    """

    # example
    @task()
    def longtask(a,b,sec):
        time.sleep(5)
