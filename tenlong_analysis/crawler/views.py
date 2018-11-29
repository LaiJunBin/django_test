from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import requests as req
from bs4 import BeautifulSoup as bs
import time
import json

# Create your views here.
def index(request):
    return render(request,'index.html')

def get_zh_tw_books(request):
    base_url = 'https://www.tenlong.com.tw'
    url = 'https://www.tenlong.com.tw/zh_tw/recent'
    books = {}
    page = 1
    while True:
        r = req.get(url + '?page=' + str(page))
        soup = bs(r.content)
        single_books = soup.select('.single-book')
        if len(single_books) == 0:
            break
        for single_book in single_books:
            single_book_soup = bs(str(single_book))
            single_book_link = single_book_soup.select('.title > a')[0]
            single_book_title = single_book_link.text
            book_url = base_url + single_book_link.attrs['href']
            book_soup = bs(req.get(book_url).content)
            book_info = book_soup.select('.item-sub-info li')
            book = {}
            for info in book_info:
                info_soup = bs(str(info))
                info_title = info_soup.select('.info-title')[0].text
                info_content =  '\n'.join(map(lambda x:x.text,info_soup.select('.info-content'))).split('\n')
                info_content = list(filter(None, map(lambda x: x.strip(),info_content)))
                book[info_title] = info_content
            books[single_book_title] = book
        page += 1
    return HttpResponse(json.dumps(books))