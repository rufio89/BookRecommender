from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import BxBooks


def index(request):
    book_list = BxBooks.objects.order_by('book_title')[:10]
    bad_img_url = 'http://images.amazon.com/images/P/0942320093.01.THUMBZZZ.jpg'
    bad_img = 'books/images/bad-image.jpg'
    context = {
        'book_list': book_list,
        'bad_img_url': bad_img_url,
        'bad_img': bad_img,
    }
    return render(request, 'books/index.html', context)

def detail(request, isbn):
    book = get_object_or_404(BxBooks, pk=isbn)
    bad_img_url = 'http://images.amazon.com/images/P/0786000015.01.LZZZZZZZ.jpg'
    bad_img = 'books/images/bad-image.jpg'
    context = {
        'isbn': isbn,
        'image_url_l': book.image_url_l,
        'book_title': book.book_title,
        'bad_img_url': bad_img_url,
        'bad_img': bad_img,
    }
    return render(request, 'books/detail.html', context)


def results(request, isbn):
    response = "You're looking at the results of book %s."
    return HttpResponse(response % isbn)