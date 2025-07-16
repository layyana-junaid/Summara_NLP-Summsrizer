import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF
import docx

from utilities.preprocessing import preprocess_text
from utilities.keyword_extractor import extract_keywords
from utilities.summarizer import summarize_minimal, summarize_bullets, summarize_insightful

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file_path):
    ext = file_path.rsplit('.', 1)[1].lower()

    if ext == 'txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    elif ext == 'pdf':
        text = ''
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    elif ext == 'docx':
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])

    return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form.get('text')
    file = request.files.get('file')
    mode = request.form.get('mode')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        text = extract_text_from_file(file_path)
        os.remove(file_path)

    if not text:
        return "Please provide text or upload a valid file.", 400

    preprocessed = ' '.join(preprocess_text(text))
    keywords = extract_keywords(text)
    keywords_string = ', '.join(keywords)

    if mode == 'minimal':
        summary = summarize_minimal(text)
    elif mode == 'bullets':
        summary = summarize_bullets(text)
    elif mode == 'insightful':
        summary = summarize_insightful(text)
    else:
        summary = ["Invalid mode selected."]

    if isinstance(summary, str):
        summary = summary.split('. ')

    return render_template('result.html', summary=summary, keywords=keywords_string, mode=mode)

if __name__ == '__main__':
    app.run(debug=True)
