from app import summarize_text
from nltk.tokenize import sent_tokenize


def test_short_text_returns_original():
    text = "Hello world. This is a test."
    summary = summarize_text(text, num_sentences=3)
    assert isinstance(summary, str)
    # For short text (<= requested sentences) should return original
    assert summary.strip() == text


def test_summary_respects_num_sentences():
    text = (
        "Cats are small domesticated carnivores. "
        "Dogs are loyal animals often kept as pets. "
        "Birds can fly and many species migrate. "
        "Fish live in water and breathe through gills."
    )
    summary = summarize_text(text, num_sentences=2)
    sentences = sent_tokenize(summary)
    assert len(sentences) <= 2
