from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('API')


def cars_by_brand(request):
    pass


def cars_model(request):
    pass


def cars_brand_model(request):
    pass
