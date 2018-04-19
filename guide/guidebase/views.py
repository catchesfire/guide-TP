from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. I fuck dog when he shits")
# Create your views here.
