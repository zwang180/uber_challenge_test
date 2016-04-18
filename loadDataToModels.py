# Setting up environment to use existing models
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uber_challenge.settings
django.setup()

# Import models
from film.models import

# Setup MongoDB
from pymongo import MongoClient
import json
import requests

# Connect to database
client = MongoClient()
db = client.uber_challenge
coll = db.film

# Remove old data before getting new data
coll.remove()

# Dump the data from provided API endpoint
r = requests.get('https://data.sfgov.org/resource/yitu-d5am.json')
data = json.loads(r.text)

for i in range(len(data)):
    curr = data[i]
    # @TODO: Create Models According to Data and Save to the DataBase
