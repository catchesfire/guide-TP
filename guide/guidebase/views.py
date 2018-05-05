from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Place
from django.template import loader



def index(request):
    all_places = Place.objects.all()
    html = ''
    for Place in all_places:
        url = '/guidebase/' + str(Place.id)
        html += '<a href="' + url + '">' + Place.name + '</a><br>'

    return HttpResponse(html)
# Create your views here.


def detail(request, place_id):
    return HttpResponse("<h2>Szczegóły dla " + str(place_id) + "</h2>")
    # template = loader.get_template('guidebase/index.html')
