from django.shortcuts import render
from main.models import Podik
from django.core import serializers
from django.http import JsonResponse

def heater(request):
    return render(request, 'main/heater.html', {})

def iqos(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 208)
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

def load_more(request):
    total_item = int(request.GET.get('total_item'))
    allObjects = Podik.objects.all().values()
    #pods = serializers.serialize('json', allObjects)[:50]
    post_obj = list(allObjects[total_item:total_item+50])
    data = {
        "podiks": post_obj,
    }
    return JsonResponse(data=data)

def homepage(request):
    allObjects = Podik.objects.all()
    pods = serializers.serialize('json', allObjects[:50])
    heaters = serializers.serialize('json', allObjects.filter(categoryId = 220)[:50])
    iqos = serializers.serialize('json', allObjects.filter(categoryId = 208)[:50])
    context = {
        "pods": pods,
        "heaters": heaters,
        "iqos": iqos,
    }
    return render(request, 'main/homepage.html', context)