import streamlit as st
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

# App title
st.set_page_config(page_title="Multilingual Sentiment Analyzer", layout="centered")
st.title("Multilingual Sentiment Analysis")
st.write("Enter multiple sentences. One sentence per line.")

# Load model (cached for performance)
@st.cache_resource
def load_model():
    model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

classifier = load_model()

# Text input
text_input = st.text_area(
    "Input text",
    height=200,
    placeholder="I love this product!\nयह बहुत अच्छा है"
)

# Analyze button
if st.button("Analyze Sentiment"):
    if not text_input.strip():
        st.warning("Please enter at least one sentence.")
    else:
        sentences = [s.strip() for s in text_input.split("\n") if s.strip()]
        results = classifier(sentences)

        st.subheader("Results")
        for sentence, result in zip(sentences, results):
            label = result["label"]

            stars = int(label.split()[0])
            if stars <= 2:
                sentiment = "Negative "
            elif stars == 3:
                sentiment = "Neutral "
            else:
                sentiment = "Positive "

            st.markdown(f"""
**Sentence:** {sentence}  
**Sentiment:** {sentiment}  
**Model Label:** {label}  
---
""")
