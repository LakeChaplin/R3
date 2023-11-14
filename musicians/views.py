from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from datetime import datetime


def index(request):  # HttpRequest
    return HttpResponse("Musician's app page")


def events(request):
    return HttpResponse('<h1> Events preview and photos</h1>')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>category_id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Categories</h1><p>category_by_slug: {cat_slug}</p>')


def archive(request, year):
    if year > datetime.now().year:
        raise Http404()
    return HttpResponse(f'<h1>Events Archive</h1><p>Year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found. 404</h1>')