from django.core.management.base import BaseCommand
from zerotask.models import Task

class Command(BaseCommand):

    args = ''
    help = (
    )

    def handle(self, *args, **options):
        t0 = Task.objects.filter(status=0).count()
        t1 = Task.objects.filter(status=1).count()
        t2 = Task.objects.filter(status=2).count()
        t3 = Task.objects.filter(status=3).count()
        print('Queued:    {}'.format(t0))
        print('Running:   {}'.format(t1))
        print('Completed: {}'.format(t2))
        print('Failed:    {}'.format(t3))
        print()
