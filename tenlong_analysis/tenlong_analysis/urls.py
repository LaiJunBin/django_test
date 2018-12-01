"""tenlong_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from crawler import views as crawler

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^crawler/', include([
        url(r'^$', crawler.index),
        url(r'^zh-tw/page/$', crawler.get_zh_tw_books),
        url(r'^zh-tw/page/(?P<page>[0-9]+)$', crawler.get_zh_tw_books_by_page),
        url(r'^zh-tw/page/max$', crawler.get_zh_tw_book_max_page),
    ])),

]
