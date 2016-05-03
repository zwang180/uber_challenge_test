from __future__ import unicode_literals

from django.db import models
from mongoengine import *

# Create your models here.
class Film(Document):
    title = StringField(required=True)
    year = IntField()
    locations = StringField(max_length=200)
    company = StringField(max_length=100)
    distributor = StringField(max_length=100)
    director = StringField(max_length=50)
    writer = StringField(max_length=50)
    actor_1 = StringField(max_length=50)
    actor_2 = StringField(max_length=50)
    actor_3 = StringField(max_length=50)
    funfacts = StringField()

    def __str__(self):
        return self.title;
