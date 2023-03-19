from django.shortcuts import render
from main.models import Podik
from django.core import serializers


def heater(request):
    return render(request, 'main/heater.html', {})

def iqos(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }
    return render(request, 'main/iqos.html', context)

def glo(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def jouz(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def powerbanks(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 282)
    }

def homepage(request):
    allObjects = Podik.objects.all()
    pods = serializers.serialize('json', allObjects)
    heaters = serializers.serialize('json', allObjects.filter(categoryId = 238))
    iqos = serializers.serialize('json', allObjects.filter(categoryId = 282))
    print(pods)
    context = {
        "pods": pods,
        "heaters": heaters,
        "iqos": iqos,
    }
    return render(request, 'main/homepage.html', context)