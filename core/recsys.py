from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

class Recommender:
    def __init__(self, movies):
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.df = pd.DataFrame(list(movies))

    def get_df(self):
        return self.df

    
