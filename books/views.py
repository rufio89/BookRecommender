from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import BxBooks, BxBookRatings
import json as simplejson
import numpy as np
import pandas as pd
from numpy import linalg as la
from django_pandas.io import read_frame


def ecludSim(inA,inB):
    return 1.0 / (1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA,inB):
    num = float(inA.T * inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5 + 0.5 * (num / denom)

def index(request):
    book_list = BxBooks.objects.order_by('book_title')[:50]
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
    results = False
    if request.is_ajax():
        template = 'books/detail.html'
        results= True
    recommend_items = recommend(isbn)
    context = {
        'isbn': isbn,
        'image_url_l': book.image_url_l,
        'book_title': book.book_title,
        'bad_img_url': bad_img_url,
        'bad_img': bad_img,
        'results': results,
        'recommend_items': recommend_items
    }

    return render(request, template, context)

def recommend(isbn):
    model_results = BxBookRatings.objects.filter(isbn=isbn).order_by('book_rating').reverse()
    similar_users = []
    [similar_users.append(x.user_id) for x in model_results]
    results = BxBookRatings.objects.filter(user_id__in=similar_users)
    similar_user_books = read_frame(results)
    isbns = np.array(similar_user_books.pivot(index='user_id', columns='isbn', values='book_rating').columns.values)
    dataMat = np.array(similar_user_books.pivot(index='user_id', columns='isbn', values='book_rating').fillna(0))
    similar_books = get_similar_books(dataMat, isbns, isbn, 5)
    final_results = BxBooks.objects.filter(isbn__in=similar_books)

    return final_results


def get_similar_books(dataMat, isbns, isbn, k, metric=ecludSim):
    isbn_index = np.where(isbns == isbn)[0][0]
    distances = []
    targets = []
    data = dataMat.T

    for i in range(len(data)):
        distance = metric(data[isbn_index], data[i])
        distances.append([distance, i])

    distances = sorted(distances, reverse=True)
    distances = distances[1:]

    for i in range(k):
        index = distances[i][1]
        targets.append(isbns[index])

    return targets



def lookup(request):
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'term'):
            value = request.GET[u'term']
            # Ignore queries shorter than length 3
            if len(value) > 2:
                model_results = BxBooks.objects.filter(book_title__icontains=value)
                results = [{'value': x.isbn, 'label':x.book_title} for x in model_results]
    json = simplejson.dumps(results)
    return HttpResponse(json)

def results(request, isbn):
    response = "You're looking at the results of book %s."
    return HttpResponse(response % isbn)