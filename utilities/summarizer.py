import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import heapq

nltk.download('punkt')
nltk.download('stopwords')

def summarize_minimal(text, sentence_count=3):
    # Tokenize sentences
    sentences = sent_tokenize(text)
    
    # Create word frequency table
    stop_words = set(stopwords.words("english"))
    words = nltk.word_tokenize(text.lower())
    words = [word for word in words if word.isalnum() and word not in stop_words]
    freq_dist = FreqDist(words)

    # Score sentences
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in freq_dist:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq_dist[word]

    # Pick top sentences
    summary_sentences = heapq.nlargest(sentence_count, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# Optional placeholders for other modes
def summarize_bullets(text):
    summary = summarize_minimal(text, sentence_count=5)
    return summary.split('. ')  # For bullet formatting

def summarize_insightful(text):
    return summarize_minimal(text, sentence_count=5)
