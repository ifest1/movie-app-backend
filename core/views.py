from rest_framework import viewsets
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from .models import Movie

from .serializers import MovieSerializer

from .recsys import Recommender
import pandas as pd

rec = Recommender(["actors", "director", "genre", "description"])
rec.init_sys(Movie.objects.all().values())

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.extra(select={'votes': 'CAST(votes as INT)'}, order_by=['votes']).reverse()
    serializer_class = MovieSerializer

    def get_paginated_response(self, data):
        return Response(data)

class Recommendation(APIView):
    def get(self, request, imdb_title_id):
        movies = rec.get_recommendations(imdb_title_id)
        movies = movies.to_dict('records')
        return Response(movies)