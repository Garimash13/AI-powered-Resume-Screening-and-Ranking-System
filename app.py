import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


st.markdown(
    """
    <style>
        body {
            background-color: #FFB6C1;  /* Baby Pink Background */
        }
        .stApp {
            background-color: #FFB6C1; /* Baby Pink */
        }
        h1, h2 {
            text-align: center;
            font-family: 'Poppins', sans-serif;
            color: #6A0572;  /* Dark Purple Text */
        }
        .stTextArea textarea {
            font-size: 18px;
            font-family: 'Poppins', sans-serif;
            color: #333;
        }
        .stFileUploader {
            text-align: center;
        }
        .css-1d391kg, .css-1cpxqw2 {
            color: #6A0572 !important; /* Dark Purple */
            font-size: 18px;
            font-weight: bold;
        }
        .dataframe {
            background-color: #fff;
            color: black;
            font-family: 'Poppins', sans-serif;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text() or ""  
    return text


def rank_resumes(job_description, resumes):
    
    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    
    job_description_vector = vectors[0].reshape(1, -1)  
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity(job_description_vector, resume_vectors).flatten()
    
    return cosine_similarities


st.markdown("<h1>🌸 AI Resume Screening & Candidate Ranking System 🌸</h1>", unsafe_allow_html=True)


st.markdown("<h2>📄 Job Description</h2>", unsafe_allow_html=True)
job_description = st.text_area("Enter the job description")


st.markdown("<h2>📂 Upload Resumes</h2>", unsafe_allow_html=True)
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.markdown("<h2>🏆 Ranking Resumes</h2>", unsafe_allow_html=True)

    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

    
    scores = rank_resumes(job_description, resumes)

    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)

    st.dataframe(results.style.set_properties(**{"background-color": "#fff", "color": "black"}))

