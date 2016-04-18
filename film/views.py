from django.shortcuts import render
from django.views import generic
from pymongo import MongoClient

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'film/index.html'
    context_object_name = 'film_name_list'

    def get_queryset(self):
        client = MongoClient()
        db = client.uber_challenge
        coll = db.film
        return coll.distinct('title')


def detail(request, title):
    client = MongoClient()
    db = client.uber_challenge
    coll = db.film
    film_locations = coll.find({'title': title}).distinct('locations')
    film_detail = coll.find_one({'title': title})
    return render(request, 'film/detail.html', {'film_detail': film_detail, 'film_locations': film_locations})
