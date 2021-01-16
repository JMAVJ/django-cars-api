from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars/brand/<str:brand>', views.cars_brand),
    path('cars/model/<str:model>', views.cars_model),
]
