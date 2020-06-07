from django.shortcuts import render, HttpResponse
# Create your views here.
import uuid

from .tasks import Tasks


def testview(request):
    Tasks.longtask(sec=1)  # example
    return HttpResponse('<h1>{}</h1>'.format(uuid.uuid4()))
