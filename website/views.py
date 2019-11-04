from django.shortcuts import render
from django.http import HttpResponse
from . import utils

def default(request):
    name = request.path.split('/')[1] + '.md'
    html = utils.convert_md_html(name)
    context = {
        'content' : html
    }

    return render(request, 'page_template.html', context=context)
