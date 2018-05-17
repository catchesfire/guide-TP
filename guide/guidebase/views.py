from django.views import generic, View
from django.shortcuts import render, redirect
from .models import Place
from .models import TypeOfPlace
from django.contrib.auth import authenticate, login, logout


class IndexView(generic.ListView):
    template_name = 'guidebase/index.html'
    context_object_name = 'recent_attraction'

    def get_queryset(self):
        return Place.objects.all().last()


class ListView(generic.ListView):
    template_name = 'guidebase/attractionlist.html'
    context_object_name = 'places'

    def get_queryset(self):
        return Place.objects.all()


class DetailIView(generic.DetailView):
    model = Place
    template_name = 'guidebase/details.html'
    context_object_name = 'attraction_object'


class LoginView(View):
    template_name = 'guidebase/login_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            error = 'Nieprawidłowy login lub hasło'
        return render(request, self.template_name, {'error_message' : error})


def logoutUser(request):
    logout(request)
    return redirect('index')


class RegisterView(View):
    template_name = 'guidebase/registration_form.html'

    def get(self, request):
        return render(request, self.template_name)



