from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('add/', addpage, name='add'),
    path('pix/', pix, name='pix'),
    path('hex/', hex, name='hex'),
    path('learn/', learn, name='learn'),
]
