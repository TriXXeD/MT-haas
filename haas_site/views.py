from django.shortcuts import render
from django.http import HttpResponse


# Test View
def index(request):
    return HttpResponse("Index site")


def plant(request):
    return HttpResponse("Plant view")


def light(request):
    return HttpResponse("Light view")


