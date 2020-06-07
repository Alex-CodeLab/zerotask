from django.db import models

# Create your models here.
from django.db import models


STATUS_CHOICES = (
    (0, 'Queued'),
    (1, 'Running'),
    (2, 'Completed'),
    (3, 'Failed'),
)


class Task(models.Model):
    """The queued task, persisted in the database
    """
    msg = models.TextField(blank=True, null=True)
    queue = models.IntegerField(null=False, default=0)
    tid = models.CharField(max_length=32)
    errormsg = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    finish_ts = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.msg
