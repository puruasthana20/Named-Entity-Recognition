# 🧠 Named Entity Recognition (NER) Web App

A sleek and interactive Named Entity Recognition (NER) web application built using **spaCy** and **Streamlit**. This project demonstrates the power of Natural Language Processing (NLP) in extracting structured information like names of people, organizations, locations, dates, and more from unstructured text.
This Named Entity Recognition model was **custom-built and trained from scratch by me, Puru Asthana**, using the spaCy NLP library. I manually labeled the dataset, trained the model, and packaged it for production use. The model is designed to identify and classify entities such as names, organizations, locations, etc., within a given text.


## 📌 Features

- Custom NER model trained using spaCy
- Clean and modern web interface with Streamlit
- Extracts and highlights entities from user-input text
- Displays entity labels such as PERSON, ORG, GPE, DATE, MONEY, etc.
- Easy to run and deploy

---


## 🧪 How to Run

### 1. Clone the repository

### 2. Install dependencies
pip install -r requirements.txt

### 3. Install the packaged model

Since GitHub limits file uploads under 25 MB, you can download and install the model from Google Drive.
### 🔗 [Download the model (.tar.gz)](https://drive.google.com/uc?id=1upbKGES-KGCHJd4oWatGH1sJ8mVQeCAR)
Then install it using pip:
pip install en_pipeline-0.0.0.tar.gz
also you can download the file from 'model file' provided in repository

## 4. Run the app:
cd ../..
streamlit run app.py


### 🧠 About the Model
Training and packaging were done using the following commands:

python -m spacy train config.cfg --output ./output --paths.train ./train.spacy --paths.dev ./dev.spacy
python -m spacy package output/model-best ner_package --force


## 💡 Use Cases
Resume Screening
Content Tagging
Knowledge Graph Construction
Information Retrieval


## 🧪 About the Training Data

The model was trained on custom annotated text using spaCy's `docbin` format and refined for accuracy. Entity types include:

- `PERSON`
- `ORG`
- `PRODUCT`

The training config used:
- Architecture: `Tok2Vec + TransitionBasedParser`
- Dropout: `0.1`


📚 Dependencies
spaCy
Streamlit
Python 3.8+

🙋‍♂️ Author
Puru Asthana
📧 puru.asthana20@gmail.com
📱 +91-8962602625
🔗 LinkedIn | GitHub

