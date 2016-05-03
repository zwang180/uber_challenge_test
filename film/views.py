from django.shortcuts import render
from django.views import generic
from pymongo import MongoClient
from film.models import Film

# Create your views here.
def index(request):
    return render(request, 'film/index.html');

class fullList(generic.ListView):
    template_name = 'film/list.html'
    context_object_name = 'film_name_list'

    def get_queryset(self):
        # client = MongoClient()
        # db = client.uber_challenge
        # coll = db.film
        return Film.objects.distinct('title').order_by('title')

def detail(request, title):
    # client = MongoClient()
    # db = client.uber_challenge
    # coll = db.film
    query = title
    film_detail = Film.objects.filter(title=query)[0]
    film_locations = Film.objects.filter(title=query).distinct('locations')
    return render(request, 'film/detail.html', {'film_detail': film_detail, 'film_locations': film_locations})

def result(request):
    # client = MongoClient()
    # db = client.uber_challenge
    # coll = db.film
    query = request.GET ['search_film_name']
    results = Film.objects.filter(title=query).distinct('title').order_by('title')

    return render(request, 'film/result.html', {'results': results})
