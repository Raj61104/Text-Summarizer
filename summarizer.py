from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import nltk
import numpy as np


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


def summarize_text(text, num_sentences=3):
    """
    Summarize the given text using TF-IDF and extract top sentences.
    
    Args:
        text (str): Input text to summarize
        num_sentences (int): Number of sentences to extract (default: 3)
    
    Returns:
        str: Summarized text
    """
    
    # Split text into sentences
    sentences = sent_tokenize(text)
    
    # If text is already small
    if len(sentences) <= num_sentences:
        return text
    
    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Score sentences
    scores = tfidf_matrix.sum(axis=1)
    scores = np.array(scores).flatten()
    
    # Get top sentence indices
    top_indices = scores.argsort()[-num_sentences:][::-1]
    
    # Keep original order
    top_indices = sorted(top_indices)
    
    # Create summary
    summary = " ".join([sentences[i] for i in top_indices])
    
    return summary
