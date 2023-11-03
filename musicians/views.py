from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("Musician's app page")


def events(request):
    return HttpResponse('<h1> Events preview and photos</h1>')