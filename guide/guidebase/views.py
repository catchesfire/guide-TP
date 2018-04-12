from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. I fuck dog when he shit")
# Create your views here.
