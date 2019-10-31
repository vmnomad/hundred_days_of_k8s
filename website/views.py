from django.shortcuts import render
from django.http import HttpResponse
import markdown

def home(request):
    context = {
        'content' : 'Default Content'
    }
    return render(request, 'index.html', context=context)
    #return HttpResponse('Hello, world!')

def about(request):
    return HttpResponse('About Me!')

def three_w(request):
    return HttpResponse('three W!')

def rules(request):
    return HttpResponse('rules!')

def resourses(request):
    return HttpResponse('resources!')

# Create your views here.
