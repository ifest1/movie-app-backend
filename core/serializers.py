from rest_framework import serializers
from .models import Movie
from .models import Account

class MovieSerializer(serializers.ModelSerializer):
    def to_representation(self, data):
        data = super(MovieSerializer, self).to_representation(data)
        data['actors'] = [field.strip(' ') for field in data.get('actors').split(',')]
        data['genre'] = [field.strip(' ') for field in data.get('genre').split(',')]
        data['language'] = [field.strip(' ') for field in data.get('language').split(',')]
        data['writer'] = [field.strip(' ') for field in data.get('writer').split(',')] if data.get('writer') != None else data.get('writer')
        return data

    class Meta:
        model = Movie
        fields = ('imdb_title_id', 'title', 'year', 'genre', 'country', 'language', 'director', 'writer', 'production_company', 'actors', 'description', 'avg_vote', 'votes', 'budget', 'metascore', 'reviews_from_users', 'reviews_from_critics')
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'password', 'username', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Account(**validated_data)
        user.set_password(password)
        user.save()
        return user

