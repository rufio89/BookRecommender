from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.cache import cache_page
from django.shortcuts import render, get_object_or_404
from .models import BxBooks, BxBookRatings
import json as simplejson
import numpy as np
import pandas as pd
from numpy import linalg as la
from django_pandas.io import read_frame
import requests
from PIL import Image
from io import BytesIO


#Different Similarity Functions for KNN
def ecludSim(inA,inB):
    return 1.0 / (1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5 * np.corrcoef(inA, inB, rowvar=0)[0][1]

def cosSim(inA,inB):
    num = float(inA.T * inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5 + 0.5 * (num / denom)

@cache_page(60*15)
#Returns the index default page
def index(request):
    return render(request, 'books/index.html')


#Gets the size of the image to see if there is an existing image
def get_image_size(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))
    return im.size

#Checks the image size to be larger than 1X1 otherwise display default image asset
def check_image_size(url):
    bad_img = 'books/images/bad-image.jpg'
    width, height = get_image_size(url)
    if width==1 and height ==1:
        url = bad_img
    return url

#Check image size for recommended list of images. Show default image asset if it doesn't exist
def check_image_size_list(items):
    bad_img = 'books/images/bad-image.jpg'
    for item in items:
        width, height = get_image_size(item.image_url_s)
        if width == 1 and height == 1:
            item.image_url_s = bad_img
    return items

@cache_page(60*15)
#Return detail data after input is submitted
def detail(request, isbn):
    book = get_object_or_404(BxBooks, pk=isbn)
    bad_img_url = 'books/images/bad-image.jpg'
    bad_img_url_l = 'books/images/bad-image-large.jpg'
    results = False
    if request.is_ajax():
        template = 'books/detail.html'
        results= True
    recommend_items = recommend(isbn)
    context = {
        'isbn': isbn,
        'bad_img_url': bad_img_url,
        'bad_img_url_l': bad_img_url_l,
        'image_url_l': check_image_size(book.image_url_l),
        'book_title': book.book_title,
        'results': results,
        'recommend_items': check_image_size_list(recommend_items)
    }

    return render(request, template, context)

#Sifts through sql tables to get data only where users have also rated the book you are searching for
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

#Does KNN on the data matrix passed in from recommend
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


#Does the lookup for the autocomplete ajax call
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



@cache_page(60*15)
#Returns whatever page for the isbn you pass in
def results(request, isbn):
    book = get_object_or_404(BxBooks, pk=isbn)
    bad_img_url = 'books/images/bad-image.jpg'
    results = False
    if request.is_ajax():
        template = 'books/detail.html'
        results = True
    recommend_items = recommend(isbn)
    context = {
        'isbn': isbn,
        'bad_img_url': bad_img_url,
        'image_url_l': check_image_size(book.image_url_l),
        'book_title': book.book_title,
        'results': results,
        'recommend_items': check_image_size_list(recommend_items)
    }
    return render(request, 'books/results.html', context)