from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .models import Movie
from .models import Account
from .models import UserFavoriteMovies

from .serializers import MovieSerializer
from .serializers import UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class Registration(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserSerializer
    permission_class = (AllowAny, )

class FavoriteMovies(APIView):
    # returns user favorite movies
    def get(self, request):
        try:
            user = Token.objects.get(key=request.headers['Token']).user
            user_favorites = user.userfavoritemovies_set.values()
            user_movies = [Movie.objects.get(imdb_title_id=user_favorite['imdb_title_id']) for user_favorite in user_favorites]
            user_movies = [MovieSerializer(user_movie).data for user_movie in user_movies]
            
            return Response(user_movies)

        except:
            return Response({'status': 'bad request'})

    # add favorite movie
    def post(self, request):
        try:
            user = Token.objects.get(key=request.headers['Token']).user
            imdb_title_id = request.data['imdb_title_id']
            movie = Movie.objects.get(imdb_title_id=imdb_title_id)
            movie = MovieSerializer(movie).data
            favorite_movie = UserFavoriteMovies(user_id=user.id, imdb_title_id=imdb_title_id)
            favorite_movie.save()

            return Response(movie)

        except:
            return Response({'status': 'bad request'})
