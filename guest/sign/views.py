from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request,"index.html",{
        'username': request.session.get('user'),
    })


def login(request):
    if request.session.get('user') is not None:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render(request,'login.html',{
            'username': request.session.get('user')
        })
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is None:
            return render(request, 'login.html', {
                'error': 'username or password error!'
            })
        
        auth.login(request,user)
        request.session['user'] = username
        return HttpResponseRedirect('/')

def guest(request):
    return render(request,'guest.html')

def event(request):
    pass

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
