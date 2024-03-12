# Import necessary libraries
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load the dataset
data = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Drop missing values
data = data.dropna(subset=['reviews.text'])

# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Add the TextBlob extension to the pipeline
nlp.add_pipe('spacytextblob')

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    # Remove stopwords and perform basic text cleaning
    return " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])

# Apply the preprocessing function to the reviews
data['reviews.text'] = data['reviews.text'].apply(preprocess_text)

# Function for sentiment analysis
def analyze_sentiment(review):
    doc = nlp(review)
    return doc._.polarity

# Apply the sentiment analysis function to the reviews
data['sentiment'] = data['reviews.text'].apply(analyze_sentiment)

# Test the model on sample reviews
sample_reviews = ["This product is amazing!", "I don't like this product.", "This product is okay."]
for review in sample_reviews:
    print(f"Review: {review}")
    print(f"Sentiment: {analyze_sentiment(review)}")

# Function to compare similarity of two reviews
def compare_reviews(review1, review2):
    doc1 = nlp(review1)
    doc2 = nlp(review2)
    return doc1.similarity(doc2)

# Compare two reviews
print(f"Review 1:{data['reviews.text'][0]}")
review1 = data['reviews.text'][0]
print(f"Review 2: {data['reviews.text'][1]}")
review2 = data['reviews.text'][1]
print(f"Similarity score: {compare_reviews(review1, review2)}")

