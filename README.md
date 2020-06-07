
Zerotask is a simple Django app for queueing jobs and processing them in the background with workers.
It uses a brokerless ZeroMQ setup, meaning that storing the queue in a database is optional.

Since it has less then 100lines of code it is extremely hackable and can be used in different setups.

Using multiple workers is currently only possible if the workers run on multiple machines (this could be avoided by using multiple ports).



## Getting started
Add `zerotask` to your INSTALLED_APPS.


All tasks should be inside the `Task` class and have
the `@task` decorator


`view.py`
```from zero.tasks import Tasks


def testview(request):
    Tasks.mytask()

```

`tasks.py`
```
class Tasks():

    # example
    @task()
    def mytask():
        time.sleep(5)
        print('...done')
```

Then start your worker.
`python worker.py`
