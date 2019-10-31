from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('3w/', views.three_w, name='three_w'),
    path('rules/', views.rules, name='rules'),
    path('resources', views.resourses, name='resources'),
]