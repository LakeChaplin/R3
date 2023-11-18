from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from datetime import datetime
from django.template.defaultfilters import join
from django.template.loader import render_to_string
from django.urls import reverse


def read_text(path: str) -> str:
    with open(path, 'r') as f:
        obj = f.read().strip()
    return obj


menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Create new article", 'url_name': 'add_article'},
        {'title': "Contact us", 'url_name': 'contact'},
        {'title': "Log in/Sing up", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Fatboy Slim', 'content': read_text('musicians/temp_info_dir/fatboy.txt'), 'is_published': True},
    {'id': 2, 'title': 'Dirtyphonics', 'content': read_text('musicians/temp_info_dir/dirty.txt'), 'is_published': True},
    {'id': 3, 'title': 'Moby', 'content': read_text('musicians/temp_info_dir/moby.txt'), 'is_published': True},
]


def index(request):  # HttpRequest
    data = {
        'title': 'Main page',
        'menu': menu,
        'posts': data_db,
    }
    template = render_to_string('musicians/index.html', context=data)
    return HttpResponse(template)


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


def show_post(request, post_id):
    return HttpResponse(f'article with id = {post_id}')


def archive(request, year):
    if year > datetime.now().year:
        uri = reverse('events')
        return redirect(uri)
    return HttpResponse(f'<h1>Events Archive</h1><p>Year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found. 404</h1>')
