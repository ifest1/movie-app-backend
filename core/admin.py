from django.contrib import admin
from .models import Movie
from .models import Account

admin.site.register(Movie)
admin.site.register(Account)
