import nltk
import re
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    # Remove special characters and digits
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
    text = re.sub(r'\d+', '', text)   # Remove digits
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.encode('ascii', 'ignore').decode()  # Remove non-ascii
    return text.strip().lower()

def preprocess_text(text):
    cleaned = clean_text(text)
    sentences = sent_tokenize(cleaned)

    processed_sentences = []
    for sent in sentences:
        words = word_tokenize(sent)
        filtered = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
        processed_sentences.append(' '.join(filtered))

    return processed_sentences
