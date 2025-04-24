# 🧠 Named Entity Recognition (NER) Web App

A sleek and interactive Named Entity Recognition (NER) web application built using **spaCy** and **Streamlit**. This project demonstrates the power of Natural Language Processing (NLP) in extracting structured information like names of people, organizations, locations, dates, and more from unstructured text.

## 🚀 Demo

![NER App Demo](https://github.com/yourusername/ner-project/assets/demo.gif)

> Try it locally and extract entities from any text!

---

## 📌 Features

- Custom NER model trained using spaCy
- Clean and modern web interface with Streamlit
- Extracts and highlights entities from user-input text
- Displays entity labels such as PERSON, ORG, GPE, DATE, MONEY, etc.
- Easy to run and deploy

---

## 📂 Project Structure


---

## 🧪 How to Run

### 1. Clone the repository
git clone https://github.com/yourusername/ner-project.git
cd ner-project 

### 2. Install dependencies
pip install -r requirements.txt

### 3. Install the packaged model
cd ner_package/en_pipeline-0.0.0/dist
pip install en_pipeline-0.0.0.tar.gz

## 4. Run the app:
cd ../..
streamlit run app.py


### 🧠 About the Model
The NER model is trained using spaCy's training config and uses the en_core_web_lg word vectors. Training and packaging were done using the following commands:

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
- Base model: `en_core_web_lg`
- Architecture: `Tok2Vec + TransitionBasedParser`
- Dropout: `0.1`
- Epochs: `∞` (early stopping via patience)


📚 Dependencies
spaCy
Streamlit
Python 3.8+

🙋‍♂️ Author
Puru Asthana
📧 puru.asthana20@gmail.com
📱 +91-8962602625
🔗 LinkedIn | GitHub

