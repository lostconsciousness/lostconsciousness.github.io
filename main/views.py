from django.shortcuts import render
from main.models import Podik


def heater(request):
    context = {
        "pods": Podik.objects.all().filter(categoryId = 238)
    }
    return render(request, 'main/heater.html', context)

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
    return render(request, 'main/homepage.html', {})
# Create your views here.
