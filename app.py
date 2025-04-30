import streamlit as st
from utils import extract_text_from_pdf, compute_similarity
import os

st.title("🤖 AI Resume Screener")
st.write("Upload a resume and job description to check similarity score.")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    if resume_file and job_desc:
        text = extract_text_from_pdf(resume_file)
        score = compute_similarity(text, job_desc)
        st.success(f"Similarity Score: {score:.2f}%")
    else:
        st.error("Please upload both resume and job description.")
