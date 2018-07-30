from django.contrib import admin

from .models import TypeOfPlace
from .models import Place
from .models import Route

admin.site.register(TypeOfPlace)
admin.site.register(Place)
admin.site.register(Route)
# Register your models here.
