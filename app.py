import streamlit as st
from summarizer import summarize_text

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📄",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1rem;
        font-weight: 600;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Text Summarizer")
st.markdown("Summarize your text using TF-IDF analysis")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Original Text")
    input_text = st.text_area(
        "Paste your text here",
        height=300,
        label_visibility="collapsed"
    )
    num_sentences = st.slider("Number of sentences:", 1, 10, 3)
    summarize_btn = st.button("🚀 Summarize", use_container_width=True)

with col2:
    st.subheader("Summary")
    output_placeholder = st.empty()

# Process summarization
if summarize_btn:
    if not input_text.strip():
        st.error("❌ Please provide text to summarize")
    else:
        try:
            with st.spinner("⏳ Summarizing..."):
                summary = summarize_text(input_text, num_sentences)
            with output_placeholder.container():
                st.text_area(
                    "Summary output",
                    value=summary,
                    height=300,
                    disabled=True,
                    label_visibility="collapsed"
                )
                st.success("✅ Summary generated successfully!")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
