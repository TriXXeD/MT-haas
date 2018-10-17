from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_url'),
    path('plants/', views.plant, name='plant_url'),
    path('lights/', views.light, name='light_url'),
]