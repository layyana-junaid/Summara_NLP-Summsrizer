from rake_nltk import Rake
import nltk
nltk.download('stopwords')

def extract_keywords(text, num_keywords=5):
    r = Rake()  # Uses stopwords for English from NLTK, and all puntuation characters.
    r.extract_keywords_from_text(text)
    ranked_phrases = r.get_ranked_phrases()

    return ranked_phrases[:num_keywords]
