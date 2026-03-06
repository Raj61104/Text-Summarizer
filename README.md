# Text Summarizer Web App

A simple web application that summarizes text using TF-IDF and NLTK. The app extracts the most important sentences from your text (number of sentences is configurable).

## Features

- 🎯 **TF-IDF Based Summarization**: Uses scikit-learn's TF-IDF algorithm to score and identify important sentences
- 📝 **Sentence Tokenization**: NLTK for accurate sentence splitting
- 💫 **Clean UI**: Modern, responsive interface with flexbox layout
- ⚡ **Real-time Summarization**: Fast processing and instant results
- 📱 **Mobile Responsive**: Works seamlessly on desktop and mobile devices

## Project Structure

```
Text-Summarizer/
├── app.py                 # Flask backend with summarization logic
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   └── index.html        # HTML frontend
└── static/
    └── style.css         # Styling with flexbox layout
```

## Requirements

- Python 3.7+
- Flask
- scikit-learn
- nltk

## Installation

### Step 1: Create a Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Or install manually:**

```bash
pip install flask scikit-learn nltk
```

## Running the App

1. Activate your virtual environment (if not already activated):

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. Run the Flask app:

```bash
python app.py
```

3. Open your browser and navigate to:

```
http://localhost:5000
```

4. Paste your text in the left box and click **"Summarize"** button

## How It Works

1. **Input**: User enters text in the left textarea
2. **Processing**:
   - Text is tokenized into sentences using NLTK
   - TF-IDF vectorizer calculates importance scores for each sentence
  - Top N sentences are selected based on highest scores (N is configurable)
   - Selected sentences are arranged in original order
3. **Output**: Summary is displayed in the right textarea

## API Endpoint

### POST /summarize

**Request:**
```json
{
  "text": "Your text to summarize here..."
}
```

**Response (Success):**
```json
{
  "summary": "Summary text here..."
}
```

**Response (Error):**
```json
{
  "error": "Error message"
}
```

## Usage Tips

- Paste longer texts (100+ words) for better results
- The app extracts up to N sentences (default 3), or returns the original if text has fewer sentences
- Common stop words (the, a, is, etc.) are ignored for more accurate scoring
- Use **Ctrl+Enter** in the text area as a shortcut to summarize

## Example

**Original Text:**
> "Machine learning is a subset of artificial intelligence. It allows computers to learn from data without being explicitly programmed. Deep learning is a specialized branch of machine learning. Neural networks are inspired by the human brain."

**Summary:**
> "Machine learning is a subset of artificial intelligence. Deep learning is a specialized branch of machine learning. Neural networks are inspired by the human brain."

## Troubleshooting

### NLTK Data Error

If you get an error about missing NLTK data:
```bash
python -m nltk.downloader punkt
```

### Port Already in Use

If port 5000 is already in use, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to 5001 or any available port
```

Then access the app at `http://localhost:5001`

## Running Tests

Run the unit tests (pytest) after installing dev dependencies:

```bash
pip install -r requirements.txt
pytest -q
```

## Future Enhancements

- Adjustable number of sentences in summary
- Multiple summarization algorithms (LSA, Sumy, etc.)
- Support for different languages
- Export summary as PDF
- Dark mode theme

## License

This project is open source and available for educational purposes.
