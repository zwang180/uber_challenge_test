from pymongo import MongoClient
import json
import requests

# Connect to database
client = MongoClient()
db = client.uber_challenge
coll = db.film_old

# Remove old data before getting new data
coll.remove()

# Dump the data from provided API endpoint
r = requests.get('https://data.sfgov.org/resource/yitu-d5am.json')
data = json.loads(r.text)

for i in range(len(data)):
    curr = data[i]
    # Remove unnecessary field
    if curr.has_key('smile_again_jenny_lee') == True:
        del curr['smile_again_jenny_lee']
    # # Insert manual id field for url query
    # curr['id'] = i + 1
    # Insert into database
    coll.insert_one(curr)
