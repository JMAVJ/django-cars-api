from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Check https://github.com/JMAVJ/django-cars-api for documentation')


def cars_brand(request, brand):
    pass


def cars_model(request, model):
    pass
