# Text Summarizer Web App

A simple web application that summarizes text using TF-IDF and NLTK. The app extracts the most important sentences from your text (number of sentences is configurable).

Built with **Streamlit** for a modern, interactive interface with zero frontend code required.

## Features

- 🎯 **TF-IDF Based Summarization**: Uses scikit-learn's TF-IDF algorithm to score and identify important sentences
- 📝 **Sentence Tokenization**: NLTK for accurate sentence splitting
- ⚡ **Lightning Fast**: Streamlit provides real-time reloading and instant results
- 📱 **Fully Responsive**: Automatic responsive design with Streamlit's layout system
- 🎨 **Modern UI**: Clean, intuitive interface with zero HTML/CSS needed
- 🚀 **Easy Deployment**: Deploy to Streamlit Cloud with one click

## Project Structure

```
Text-Summarizer/
├── app.py                 # Streamlit main application
├── summarizer.py          # Text summarization logic
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── tests/
│   └── test_summarizer.py # Unit tests
└── venv/                  # Virtual environment
```

## Requirements

- Python 3.8+
- Streamlit
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

## Running the App

1. Activate your virtual environment (if not already activated):

```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. Run the Streamlit app:

```bash
streamlit run app.py
```

3. Your browser will automatically open to:

```
http://localhost:8501
```

4. Paste your text in the left box, adjust the number of sentences (1-10), and click **"🚀 Summarize"**

## How It Works

1. **Input**: User enters text in the left textarea
2. **Processing**:
   - Text is tokenized into sentences using NLTK
   - TF-IDF vectorizer calculates importance scores for each sentence
   - Top N sentences are selected based on highest scores (N is configurable)
   - Selected sentences are arranged in original order
3. **Output**: Summary is displayed in the right textarea

## Code Structure

**Request:**
```json
{
  "text": "Your text to summarize here..."
}
```

## Usage Tips

- Paste longer texts (100+ words) for better results
- The app extracts up to N sentences (1-10, default 3), or returns the original if text has fewer sentences
- Common stop words (the, a, is, etc.) are ignored for more accurate scoring
- Click the **"🚀 Summarize"** button to generate your summary

## Example

**Original Text:**
> "Machine learning is a subset of artificial intelligence. It allows computers to learn from data without being explicitly programmed. Deep learning is a specialized branch of machine learning. Neural networks are inspired by the human brain."

**Summary (3 sentences):**
> "Machine learning is a subset of artificial intelligence. Deep learning is a specialized branch of machine learning. Neural networks are inspired by the human brain."

## Troubleshooting

### NLTK Data Error

If you get an error about missing NLTK data, the app will automatically download it on first run.

### Port Already in Use

The default Streamlit port is 8501. If you want to use a different port:
```bash
streamlit run app.py --server.port 8502
```

## Running Tests

Run the unit tests (pytest) with:

```bash
pytest -q
```

The summarizer logic is in `summarizer.py` and can be tested independently from the Streamlit frontend.

## Deployment

### Deploy to Streamlit Cloud (Free)

1. Push your project to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **"New app"** and select your repository
4. It will deploy automatically!

### Deploy Elsewhere

- **Heroku**: see `Procfile` example below
- **AWS/GCP**: Use Docker
- **Railway**: Connect GitHub repo directly

## Future Enhancements

- Multiple summarization algorithms (LSA, Sumy, etc.)
- Support for different languages
- Export summary as PDF
- Language detection
- Batch summarization

## License

This project is open source and available for educational purposes.
