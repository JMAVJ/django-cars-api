from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('API')


def cars_brand(request, brand):
    pass


def cars_model(request, model):
    pass
