from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index_url'),
    path('plants/', views.plant_overview, name='plant_url'),
    path('plants/<int:plant_id>/', views.plant, name='plant_specific'),
    path('lights/', views.light_overview, name='light_url'),
]