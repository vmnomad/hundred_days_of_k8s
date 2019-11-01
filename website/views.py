from django.shortcuts import render
from django.http import HttpResponse
import markdown

def home(request):
    context = {
        'content' : 'This text is built dynamiccaly by Django View function'
    }
    print("Path", request.path)
    return render(request, 'index.html', context=context)
    #return HttpResponse('Hello, world!')

def about(request):

    return HttpResponse('About Me!')

def three_w(request):
    context = {
        'content' : 'This is 3Ws page'
    }
    print("Path", request.path)
    return render(request, '3w.html', context=context)

def rules(request):
    return HttpResponse('rules!')

def resourses(request):
    return HttpResponse('resources!')

# Create your views here.
