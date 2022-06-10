from django.conf import settings
from django.shortcuts import render
from .models import SpaceObject


def home_view(request):
    planets = SpaceObject.objects.filter(type=settings.SPACE_OBJECT_TYPE[0][0])
    template = 'index.html'
    return render(request, template, {'planets': planets})
