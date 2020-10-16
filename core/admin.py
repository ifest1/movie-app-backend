from django.contrib import admin
from .models import Movie
from .models import Account
from .models import UserFavoriteMovies
from .models import UserSuggestions

admin.site.register(Movie)
admin.site.register(Account)
admin.site.register(UserFavoriteMovies)
admin.site.register(UserSuggestions)
