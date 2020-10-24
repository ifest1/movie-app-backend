from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        data = super(MovieSerializer, self).to_representation(data)
        data['actors'] = [field.strip(' ') for field in data.get('actors').split(',')] if data.get('actors') != None else ''
        data['genre'] = [field.strip(' ') for field in data.get('genre').split(',')] if data.get('genre') != None else ''
        data['language'] = [field.strip(' ') for field in data.get('language').split(',')] if data.get('language') != None else ''
        data['writer'] = [field.strip(' ') for field in data.get('writer').split(',')] if data.get('writer') != None else data.get('writer')
        return data

    class Meta:
        model = Movie
        fields = ('imdb_title_id', 'title', 'year', 'genre', 'country', 'language', 'director', 'writer', 'production_company', 'actors', 'description', 'avg_vote', 'votes', 'budget', 'metascore', 'reviews_from_users', 'reviews_from_critics')
    