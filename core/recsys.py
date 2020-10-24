from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

class Recommender:
    def __init__(self, features):
        self.count = CountVectorizer(stop_words='english')
        self.features = features

        self.df = None
        self.count_matrix = None
        self.indices = None
        self.cosine_sim = None

    def init_sys(self, movies):
        self.df = pd.DataFrame(list(movies))
        
        self.set_actors()
        self.set_directors()
        self.set_genres()
        self.set_description()
        self.set_soup()

        self.build_count_matrix()
        self.build_indices()
        self.build_similarities()

    def get_recommendations(self, imdb_title_id):
        idx = self.indices[imdb_title_id]

        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        
        movie_indices = [i[0] for i in sim_scores]
        
        return self.df.iloc[movie_indices][['imdb_title_id', 
        'title',
        'director', 
        'genre',
        'actors',
        'description',
        'year',
        'writer',
        'avg_vote', 
        'production_company',
        'language',
        'country',
        'votes',
        'budget',
        'metascore',
        'reviews_from_users',
        'reviews_from_critics']]

    def get_movies(self):
        return self.df

    def build_count_matrix(self):
        self.count_matrix = self.count.fit_transform(self.df['soup'])

    def build_indices(self):
        self.df.reset_index()
        self.indices = pd.Series(self.df.index, index=self.df['imdb_title_id'])

    def build_similarities(self):
        self.cosine_sim = cosine_similarity(self.count_matrix, self.count_matrix)

    def set_actors(self):
        self.df['actors'] = self.df['actors'].str.strip()
        self.df['actors_s'] = self.df['actors'].str.lower()
        self.df['actors_s'] = self.df['actors_s'].str.split(',')[1:3]
        self.df['actors'] = self.df['actors'].str.split(',')
        self.df['actors_s'] = self.df['actors_s'].fillna('')

    def set_directors(self):
        self.df['director'] = self.df['director'].str.strip()
        self.df['director_s'] = self.df['director'].str.lower()
        self.df['director_s'] = self.df['director_s'].str.split(',')
        self.df['director'] = self.df['director'].str.split(',')
        self.df['director_s'] = self.df['director_s'].fillna('')

    def set_genres(self):
        self.df['genre'] = self.df['genre'].str.strip()
        self.df['genre_s'] = self.df['genre'].str.lower()
        self.df['genre_s'] = self.df['genre_s'].str.split(',')
        self.df['genre'] = self.df['genre'].str.split(',')

    def set_country(self):
        self.df['country'] = self.df['country'].str.strip()
        self.df['country'] = self.df['country'].str.split(',')
        self.df['country'] = self.df['country'].fillna('')

    def set_description(self):
        self.df['description_s'] = self.df['description'].fillna('')
        self.df['description_s'] = self.df['description_s'].str.lower()

    def set_soup(self):
        self.df['soup'] = self.df.apply(self.create_soup, axis=1)

    def create_soup(self, x):
        x['actors_s'] = ' '.join(x['actors_s'])
        x['director_s'] = ' '.join(x['director_s'])
        x['genre_s'] = ' '.join(x['genre_s'])

        return x['actors_s'] + x['director_s'] * 3 + x['description_s']