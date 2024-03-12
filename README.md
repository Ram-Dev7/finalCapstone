# finalCapstone

# Project Name: Amazon Product Reviews Sentiment Analysis

## Description:
This project focuses on sentiment analysis of Amazon product reviews using natural language processing (NLP) techniques. It utilizes the spaCy library with the spaCyTextBlob extension to preprocess text and perform sentiment analysis. The goal is to help users understand the overall sentiment expressed in Amazon product reviews.

## Importance:
Understanding customer sentiment is crucial for businesses to gauge the reception of their products in the market. This sentiment analysis tool provides a quick and automated way to analyze the sentiment of Amazon product reviews, allowing businesses to gain valuable insights into customer opinions.

## Table of Contents:
1. [Installation](#installation)
2. [Usage](#usage)
3. [Sample Reviews](#sample-reviews)
4. [Similarity Comparison](#similarity-comparison)
5. [Credits](#credits)

## Installation:
To run the code locally, follow these steps:
- Make sure you have Python installed (version 3.6 or later).
- Install the required libraries using the following command:
  ```bash
  pip install pandas spacy spacytextblob
  ```

## Usage:
1. Clone the repository or download the script.
2. Ensure the 'amazon_product_reviews.csv' file is in the same directory as the script.
3. Run the script, and it will perform sentiment analysis on the Amazon product reviews.

## Sample Reviews:
You can test the sentiment analysis with the following sample reviews:
- "This product is amazing!"
- "I don't like this product."
- "This product is okay."

```python
# Test the model on sample reviews
sample_reviews = ["This product is amazing!", "I don't like this product.", "This product is okay."]
for review in sample_reviews:
    print(f"Review: {review}")
    print(f"Sentiment: {analyze_sentiment(review)}")
```

## Similarity Comparison:
You can also compare the similarity of two reviews using the `compare_reviews` function.

```python
# Compare two reviews
print(f"Review 1:{data['reviews.text'][0]}")
review1 = data['reviews.text'][0]
print(f"Review 2: {data['reviews.text'][1]}")
review2 = data['reviews.text'][1]
print(f"Similarity score: {compare_reviews(review1, review2)}")
```

## Credits:
- This project was created by Ram.
- Special thanks to the developers of spaCy and spaCyTextBlob for their contributions.

Feel free to explore and customize the code for your specific use case!