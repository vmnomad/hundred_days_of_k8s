from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path(r'', RedirectView.as_view(url='/home/')), # redirect to home url to let view get the md file name from url
    path('hom/', views.default, name='home'),
    path('about/', views.default, name='about'),
    path('3w/', views.default, name='three_w'),
    path('rules/', views.default, name='rules'),
    path('resources/', views.default, name='resources'),
]