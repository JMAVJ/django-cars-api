from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cars/<str:brand>', views.cars_by_brand),
    path('cars/<str:model>', views.cars_model),
    path('cars/<str:brand>/<str:model>', views.cars_brand_model),
]
