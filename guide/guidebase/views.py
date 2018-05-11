from django.views import generic
from .models import Place
from .models import TypeOfPlace


class IndexView(generic.ListView):
    template_name = 'guidebase/index.html'
    context_object_name = 'recent_attraction'
    def get_queryset(self):
        return Place.objects.all().last()

class ListView(generic.ListView):
    template_name = 'guidebase/attractionlist.html'

    def get_queryset(self):
        return Place.objects.all()


class DetailIView(generic.DetailView):
    model = Place
    template_name = 'guidebase/detail.html'
