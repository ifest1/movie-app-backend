from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

class Movie(models.Model):
    imdb_title_id = models.CharField(primary_key=True, max_length=45)
    title = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    year = models.CharField(max_length=20)
    date_published = models.CharField(max_length=20)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    country = models.CharField(max_length=45)
    language = models.CharField(max_length=45)
    director = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    production_company = models.CharField(max_length=100)
    actors = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    avg_vote = models.CharField(max_length=20)
    votes = models.CharField(max_length=20)
    budget = models.CharField(max_length=30)
    usa_gross_income = models.CharField(max_length=45)
    worldwide_gross_income = models.CharField(max_length=45)
    metascore = models.CharField(max_length=45)
    reviews_from_users = models.CharField(max_length=45)
    reviews_from_critics =models.CharField(max_length=45)
    