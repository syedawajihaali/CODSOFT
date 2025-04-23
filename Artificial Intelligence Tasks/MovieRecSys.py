import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    'title': [
        'The Matrix', 'John Wick', 'Inception', 'Interstellar',
        'The Notebook', 'La La Land', 'Avengers: Endgame', 'Iron Man'
    ],
    'description': [
        'A computer hacker learns about the true nature of reality.',
        'An ex-hitman comes out of retirement to track down gangsters.',
        'A thief steals corporate secrets through dream-sharing technology.',
        'A team travels through a wormhole to ensure humanity’s survival.',
        'A love story between a poor man and a rich woman.',
        'A jazz musician and an aspiring actress fall in love.',
        'Superheroes unite to undo the damage done by Thanos.',
        'A billionaire becomes a tech-based superhero.'
    ]
}

# Load data
df = pd.DataFrame(data)

# TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies
def recommend(title, df=df, cosine_sim=cosine_sim):
    if title not in df['title'].values:
        return "Movie not found in the database."
    
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]
    recommended_titles = [df.iloc[i[0]]['title'] for i in sim_scores]
    return recommended_titles

# Display movies
print("Available Movies:")
for idx, movie in enumerate(df['title'], 1):
    print(f"{idx}. {movie}")

# Ask for user input
choice = input("\nEnter the movie name you like (exact match): ")

# Get recommendations
recommendations = recommend(choice)

# Show results
print("\nRecommended Movies:")
if isinstance(recommendations, list):
    for movie in recommendations:
        print(f"- {movie}")
else:
    print(recommendations)


