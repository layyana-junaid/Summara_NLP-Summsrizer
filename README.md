# Summara - Your Personal Summarizer!
![Summara](https://github.com/user-attachments/assets/eb605d7d-5298-4de0-b5c5-f6feb2937a10)


### Overview:
#### Summara is a lightweight and interactive web application designed to simplify the task of summarizing large texts. It supports multiple file formats and provides three styles of summarization: Minimal, Bullet Points, and Insightful. Summara also extracts key points, offering users a quick and informative overview of lengthy documents. With an emphasis on friendly UI and visual appeal, Summara includes thematic mascots and a polished front-end.

graph TD
    A[User Launches App] --> B[Paste Text / Upload File]
    B --> C[Flask Receives Request]
    C --> D[Preprocess Text]
    D --> E{Selected Mode?}
    E -->|Minimal| F[Minimal Summary]
    E -->|Bullets| G[Bullet Summary]
    E -->|Insightful| H[Insightful Summary]
    F --> I[Extract Keywords]
    G --> I
    H --> I
    I --> J[Render result.html]
    J --> K[Show Summary + Key Details]


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
### WorkFlow:
![first](https://github.com/user-attachments/assets/8ef66c2f-3993-4610-b711-ea9e8281ce83)

![second](https://github.com/user-attachments/assets/71525782-2dea-4bf1-b657-b3658d0abc22)

![third](https://github.com/user-attachments/assets/3022250f-94dc-4133-83ca-54a2c58546f8)

![fourth](https://github.com/user-attachments/assets/314a8d0a-16d5-48b8-8999-ed2109f781a6)


