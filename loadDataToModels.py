# Setting up environment to use existing models
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uber_challenge.settings")
django.setup()

# Import models
from film.models import Film

# Setup MongoDB
from pymongo import MongoClient
import json
import requests

# Connect to database
client = MongoClient("mongodb://zwang180:Aa527710546@ds059155.mlab.com:59155/sf_film")
# client = MongoClient()
db = client.sf_film
# db = client.uber_challenge
coll = db.film

# Remove old data before getting new data
coll.remove()

# Dump the data from provided API endpoint
r = requests.get('https://data.sfgov.org/resource/yitu-d5am.json')
data = json.loads(r.text)
total = len(data)

for i in range(total):
    curr = data[i]

    if curr.has_key('smile_again_jenny_lee') == True:
        del curr['smile_again_jenny_lee']
    doc = Film.objects.create(title=curr['title'], year=curr['release_year'], company=curr['production_company'], director=curr['director'])

    if curr.has_key('writer') == True:
        doc.writer = curr['writer']
    if curr.has_key('locations') == True:
        doc.locations = curr['locations']
    if curr.has_key('distributor') == True:
        doc.distributor = curr['distributor']
    if curr.has_key('actor_1') == True:
        doc.actor_1 = curr['actor_1']
    if curr.has_key('actor_2') == True:
        doc.actor_2 = curr['actor_2']
    if curr.has_key('actor_3') == True:
        doc.actor_3 = curr['actor_3']
    if curr.has_key('fun_facts') == True:
        doc.funfacts = curr['fun_facts']
    doc.save()
    print(str(i + 1) + '/' + str(total))
# TODO Save to mLab database
