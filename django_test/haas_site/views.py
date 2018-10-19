from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Plant, LightGroup, LightBulb


# Test View
def index(request):
    plant_list = Plant.objects.order_by('humidity')
    # plant_response = []
    # for p in plant_list:
    #     plant_response.append("Name: " + p.name + ", Humidity: " + str(p.humidity) + " \n")
    # return HttpResponse(response, content_type="text/plain")
    template = loader.get_template('haas_site/index.html')
    context = {
        'plant_list': plant_list,
    }
    return HttpResponse(template.render(context, request))


def plant_overview(request):
    return HttpResponse("Plant view")


def plant(request, plant_id):
    respones = "Values for plant: %s"
    return HttpResponse(respones % plant_id)


def light_overview(request):
    return HttpResponse("Light view")


