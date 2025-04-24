import spacy
import streamlit as st

# Load the pre-trained SpaCy NER model
nlp = spacy.load("en_pipeline")  # Changed to standard available model

# Page configuration
st.set_page_config(page_title=" NER Demo", layout="wide")

# Inject custom CSS for improved styling
st.markdown("""
    <style>
        html, body {
            background-color: #f4f6f6;
        }
        .title {
            font-size: 50px;
            font-weight: bold;
            color: white;
            text-align: center;
            background: linear-gradient(to right, #f12711, #f5af19);
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .instruction {
            text-align: center;
            font-size: 18px;
            color: #333;
            margin-bottom: 40px;
        }
        .entity {
            background-color: #17202a;
            padding: 10px;
            border-left: 5px solid #ff6f00;
            margin: 10px 0;
            border-radius: 8px;
            font-size: 16px;
        }
        .footer {
            text-align: center;
            padding: 15px;
            margin-top: 40px;
            font-size: 14px;
            color: #888;
            border-top: 1px solid #ddd;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<div class="title">Named Entity Recognition with SpaCy</div>', unsafe_allow_html=True)

# Instructions
st.markdown('<div class="instruction">💡 Enter any text below, and we’ll highlight entities like names, locations, organizations, and more.</div>', unsafe_allow_html=True)

# Text input
text = st.text_area("Enter text for NER:", height=200, placeholder="Type or paste your text here...")

# NER Processing and Display
if text:
    doc = nlp(text)
    with st.container():
        if doc.ents:
            st.markdown("### 🎯 Recognized Entities")
            for ent in doc.ents:
                st.markdown(f"<div class='entity'><strong>{ent.text}</strong> — <span style='color:#d35400'>{ent.label_}</span></div>", unsafe_allow_html=True)
        else:
            st.info("🔍 No named entities found. Try a different or longer sentence.")

# Footer
st.markdown('<div class="footer">Made by Puru Asthana</div>', unsafe_allow_html=True)
