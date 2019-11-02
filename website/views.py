from django.shortcuts import render
from django.http import HttpResponse
from . import utils

def default(request):

    if request.path == '/':
        html = utils.convert_md_html('home.md')
        context = {
            'content' : html
        }

        return render(request, 'index.html', context=context)
    
    
    elif request.path == '/3w/':
        html = utils.convert_md_html('3w.md')
        context = {
            'content' : html
        }

        return render(request, '3w.html', context=context)
