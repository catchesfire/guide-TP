from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('guidebase/index.html')
    return HttpResponse(template.render())
# Create your views here.


def detail(request, place_id):
    return HttpResponse("<h2>Szczegoly dla " + str(place_id) + "</h2>")
