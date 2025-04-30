# Resume Screener using AI (NLP + Streamlit)
This app compares a resume PDF to a job description and outputs a similarity score.

## Features
- PDF resume parsing
- TF-IDF cosine similarity
- Streamlit interface

- Paste a job description
- 
## Teck Stack

- Python
  
- Streamlit
 
- scikit-learn
  
- PyPDF2
  
- TF-IDF & Cosine Similarity (NLP)
  

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Requirements

- Python 3.7+

- Internet browser (for Streamlit UI)

## How It Works
- Extracts raw text from PDF resume

- Compares it with the job description using TF-IDF vectorization

- Computes a similarity score using cosine similarity

- Displays the match percentage
