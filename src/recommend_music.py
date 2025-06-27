import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

class MusicRecommendationSystem:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.embeddings = None
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def initialize(self):
        try:
            self.df = pd.read_csv(self.csv_path)
            required = ['Title', 'Mood', 'Genre', 'Language']
            if any(col not in self.df.columns for col in required):
                return "❌ Dataset missing required columns."
            
            text_data = self.df['Title'] + ' ' + self.df['Mood'] + ' ' + self.df['Genre'] + ' ' + self.df['Language']
            self.embeddings = self.model.encode(text_data.tolist(), convert_to_tensor=True)
            return None
        except Exception as e:
            return f"❌ Error loading CSV or embeddings: {str(e)}"

    def get_unique_genres(self):
        return sorted(self.df['Genre'].dropna().unique())

    def recommend(self, caption, genre, top_n=5):
        query = f"{caption} {genre}"
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        similarity_scores = util.cos_sim(query_embedding, self.embeddings)[0]
        top_indices = similarity_scores.argsort(descending=True)[:top_n].cpu().numpy()
        top_songs = self.df.iloc[top_indices]
        dominant_mood = top_songs['Mood'].mode()[0] if not top_songs.empty else "Unknown"
        return top_songs, dominant_mood