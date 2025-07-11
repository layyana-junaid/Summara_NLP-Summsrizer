# Summara - Your Personal Summarizer

### Overview:
#### Summara is a lightweight and interactive web application designed to simplify the task of summarizing large texts. It supports multiple file formats and provides three styles of summarization: Minimal, Bullet Points, and Insightful. Summara also extracts key points, offering users a quick and informative overview of lengthy documents. With an emphasis on friendly UI and visual appeal, Summara includes thematic mascots and a polished front-end.

### Goals:
Provide an intuitive and visually appealing platform to summarize text content.
Enable users to upload .txt, .pdf, and .docx files.
Offer multiple styles of summarization tailored to user preferences.
Display extracted keywords or key ideas from the content.


### Technologies Used:
### Backend:
```
Flask: Python micro-framework to manage routing and server-side logic.
Werkzeug: Handles secure file uploads.
PyMuPDF (fitz): Extracts text content from .pdf files.
python-docx: Parses text from .docx files.
```

### Custom Modules:
```
preprocessing.py: Tokenizes and cleans input text.
keyword_extractor.py: Extracts significant terms using frequency and scoring methods.
summarizer.py: Offers three summarization strategies:
summarize_minimal
summarize_bullets
summarize_insightful
```
### Frontend:
```
HTML5/CSS3: Core structure and styling.
Google Fonts: Utilizes 'Berkshire Swash' and 'Fraunces' for branding and aesthetic appeal.
Responsive Design: Adjusts layout based on screen size.
Mascot Art: Custom illustrations of an owl and a penguin for a friendly UI theme.
User Interface Features:
Upload or paste text directly.
Choose summary style from a dropdown.
Display of summary and extracted keywords.
```
