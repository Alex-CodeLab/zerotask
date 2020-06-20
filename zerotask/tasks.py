import time
from .decorator import task

###################

class Tasks():
    """ Any function can be offloaded to the worker by using the @task decorator
        Note that when a function is called by the worker, the arguments are
        parsed as string.
        Default queue = 0 , to set different queue: @task(queue=6)
    """

    # example
    @task()
    def longtask(*args, **kwargs):
        sec = kwargs['sec']
        time.sleep(sec)
