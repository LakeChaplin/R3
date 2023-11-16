from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from datetime import datetime

from django.template.loader import render_to_string
from django.urls import reverse

menu = ['About', 'Create new article', 'Contact us', 'Log in/Sing up']


def index(request):  # HttpRequest
    data = {
        'title': 'Main page',
        'menu': menu,
    }
    template = render_to_string('musicians/index.html', context=data)
    return HttpResponse(template)


def about(request):
    data = {
        'title': 'About us'
    }
    return render(request, 'musicians/about.html', context=data)


def events(request):
    return HttpResponse('<h1> Events preview and photos</h1>')


def categories_id(request, cat_id):
    return HttpResponse(f'<h1>Categories</h1><p>category_id: {cat_id}</p>')


def categories(request, cat_slug):
    return HttpResponse(f'<h1>Categories</h1><p>category_by_slug: {cat_slug}</p>')


def archive(request, year):
    if year > datetime.now().year:
        uri = reverse('events')
        return redirect(uri)
    return HttpResponse(f'<h1>Events Archive</h1><p>Year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found. 404</h1>')
