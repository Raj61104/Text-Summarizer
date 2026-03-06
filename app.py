from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
import nltk
import numpy as np


try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)

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


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/summarize', methods=['POST'])
def summarize():
    """Handle text summarization request."""
    try:
        data = request.get_json() or {}
        text = (data.get('text') or '').strip()

        # Get number of sentences (optional)
        num_sentences = data.get('num_sentences', 3)
        try:
            num_sentences = int(num_sentences)
        except (TypeError, ValueError):
            return jsonify({'error': 'num_sentences must be an integer'}), 400

        # Validate input
        if not text:
            return jsonify({'error': 'Please provide text to summarize'}), 400
        if num_sentences < 1:
            return jsonify({'error': 'num_sentences must be >= 1'}), 400

        # Summarize
        summary = summarize_text(text, num_sentences=num_sentences)

        return jsonify({'summary': summary, 'num_sentences': num_sentences}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)
