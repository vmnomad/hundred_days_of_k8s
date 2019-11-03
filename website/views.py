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
    
    
    else:
        name = request.path.split('/')[1] + '.md'
        html = utils.convert_md_html(name)
        context = {
            'content' : html
        }

        return render(request, '3w.html', context=context)

