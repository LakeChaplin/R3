from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),  # http://127.0.0.1:8000/
    path('events/', views.events, name='events'),  # http://127.0.0.1:8000/events
    path('archive/<year4:year>/', views.archive, name='archive'),  # http://127.0.0.1:8000/archive/slug2/
    path('about/', views.about, name='about'),  # http://127.0.0.1:8000/about
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('add_article/', views.add_article, name='add_article'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
