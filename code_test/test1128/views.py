from django.shortcuts import render
from django.http import HttpResponse

from bs4 import BeautifulSoup as bs
import requests as req
import json 

# Create your views here.

def index(request):
    # return HttpResponse("Hello world")
    if request.method == 'GET':
        return render(request,'index.html')
    elif request.method == 'POST':
        request.session['uri'] = request.POST.get('uri')
        return render(request,'code.html')

def get_format(request):
    uri = request.session.get('uri')
    r = req.get(uri)
    return HttpResponse(r.content)

def get_code(request):
    uri = request.session.get('uri')
    r = req.get(uri)
    soup = bs(r.content)
    code = soup.select('.static-editor-code')[0]
    gutter = soup.select('.static-editor-gutter')[0] 
    return HttpResponse(json.dumps({
        'code': code.text,
        'gutter': gutter.text
    }))