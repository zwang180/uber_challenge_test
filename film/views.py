from django.shortcuts import render
from django.views import generic
from pymongo import MongoClient

# Create your views here.
class fullList(generic.ListView):
    template_name = 'film/list.html'
    context_object_name = 'film_name_list'

    def get_queryset(self):
        client = MongoClient()
        db = client.uber_challenge
        coll = db.film
        return coll.distinct('title')

def index(request):
    return render(request, 'film/index.html');

def detail(request, title):
    client = MongoClient()
    db = client.uber_challenge
    coll = db.film
    film_locations = coll.find({'title': title}).distinct('locations')
    film_detail = coll.find_one({'title': title})
    return render(request, 'film/detail.html', {'film_detail': film_detail, 'film_locations': film_locations})

def result(request):
    client = MongoClient()
    db = client.uber_challenge
    coll = db.film
    query = request.GET ['search_film_name']
    results = coll.find({'title': query}).distinct('title')

    return render(request, 'film/result.html', {'results': results})
