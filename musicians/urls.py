from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index),  # http://127.0.0.1:8000/
    path('events/', views.events),  # http://127.0.0.1:8000/events
    path('categories/<int:cat_id>/', views.categories),  # http://127.0.0.1:8000/categories/2/
    path('categories/<slug:cat_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/categories/slug2/
    path('archive/<year4:year>/', views.archive),  # http://127.0.0.1:8000/archive/slug2/
]
