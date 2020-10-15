from rest_framework import serializers
from .models import Movie
from .models import Account

class MovieSerializer(serializers.ModelSerializer):
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
