from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event

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
    return render(request,'guest.html',{
        'username': request.session.get('user'),
        'events': Event.objects.all()
    })


def event(request):
    pass

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def guest_add(request):
    if request.method == 'GET':
        return render(request,'guest_add.html',{
            'username': request.session.get('user'),
        })
    elif request.method == 'POST':
        name = request.POST.get('name')
        limit = request.POST.get('limit')
        address = request.POST.get('address')
        event_time = request.POST.get('event_time')
        try:
            Event.objects.create(name = name, limit = limit, address = address, status = True, start_time = event_time)
            return HttpResponseRedirect('/guest')
        except:
            return render(request,'guest_add.html',{
                'username': request.session.get('user'),
                'error': '輸入格式錯誤!'
            })

