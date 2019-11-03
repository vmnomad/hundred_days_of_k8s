from django.urls import path
from . import views

urlpatterns = [
    path('', views.default, name='home'),
    path('about', views.default, name='about'),
    path('3w', views.default, name='three_w'),
    path('rules', views.default, name='rules'),
    path('who', views.default, name='who'),
    path('resources', views.default, name='resources'),
]