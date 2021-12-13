from django.urls import path

from main.views import *

urlpatterns = [
    path('', index, name='home'),
    path('add/', addpage, name='add'),
    path('pix/', pix, name='pix'),
]
