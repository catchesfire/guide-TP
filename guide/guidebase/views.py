from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Place
from django.template import loader


def index(request):
    all_places = Place.objects.all()

    template = loader.get_template('guidebase/index.html')
    context = {
        'all_places' : all_places,
        'x' : Place.objects.count(),
    }
    return HttpResponse(template.render(context, request))
# Create your views here.


def detail(request, place_id):
    return HttpResponse("<h2>Szczegóły dla " + str(place_id) + "</h2>")
    # template = loader.get_template('guidebase/index.html')
