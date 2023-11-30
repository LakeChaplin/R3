from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.template.defaultfilters import join
from django.template.loader import render_to_string
from django.urls import reverse
from .models import *


def read_text(path: str) -> str:
    with open(path, 'r') as f:
        obj = f.read().strip()
    return obj


menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Create new article", 'url_name': 'add_article'},
        {'title': "Contact us", 'url_name': 'contact'},
        {'title': "Log in/Sing up", 'url_name': 'login'}
        ]


def index(request):  # HttpRequest
    posts = Musicians.published.all()
    data = {
        'title': 'Legends of electronic music',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
    }

    return render(request, 'musicians/index.html', context=data)


def about(request):
    return render(request, 'musicians/about.html', {'title': 'About site', 'menu': menu})


def contact(request):
    return HttpResponse('Contact us page')


def login(request):
    return HttpResponse('Log in/ Sing up page (authorisation)')


def add_article(request):
    return HttpResponse('Page for create new article')


def events(request):
    return HttpResponse('<h1> Events preview and photos</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Musicians, slug=post_slug)
    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'musicians/post.html', context=data)


def archive(request, year):
    if year > datetime.now().year:
        uri = reverse('events')
        return redirect(uri)
    return HttpResponse(f'<h1>Events Archive</h1><p>Year: {year}</p>')


def show_category(request, cat_slug):
    category = get_object_or_404(Categories, slug=cat_slug)
    posts = Musicians.published.filter(category_id=category.pk)
    data = {
        'title': f'Legends of {category.name} music',
        'menu': menu,
        'posts': posts,
        'cat_selected': category.pk,
    }

    return render(request, 'musicians/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found. 404</h1>')
