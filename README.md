# AI-powered-Resume-Screening-and-Ranking-System
📌 Overview
The AI-Powered Resume Screening and Ranking System is a Streamlit-based web application that helps recruiters efficiently screen and rank resumes based on a given job description. It utilizes Natural Language Processing (NLP) techniques, specifically TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity, to determine how well each resume matches the job requirements.

🎯 Features

✅ Upload multiple resumes (PDF format)
✅ Enter a job description for comparison
✅ AI-driven ranking based on relevance
✅ Intuitive and visually appealing interface with a baby pink theme
✅ Fast and accurate resume scoring using NLP

🛠️ Technologies Used

Python 🐍
Streamlit (for web UI)
PyPDF2 (to extract text from PDFs)
scikit-learn (for NLP & similarity scoring)
Pandas (for data handling)

🚀 How It Works?
Input Job Description: Enter the job description in the text area.
Upload Resumes: Upload multiple PDF resumes.
AI Analysis: The system extracts text, computes TF-IDF vectors, and calculates cosine similarity.
Ranking Display: The resumes are ranked based on their similarity scores.

📦 Installation & Setup

1️⃣ Prerequisites
Ensure you have Python 3.8+ installed. You can download it from Python's official website.

2️⃣ Install Dependencies
Run the following command to install required Python libraries:
pip install streamlit PyPDF2 pandas scikit-learn

3️⃣ Run the Application
Use the command below to start the app:
streamlit run app.py
This will launch the app in your web browser.

💡 Future Enhancements
🔹 Add support for DOCX file uploads
🔹 Include keyword-based filtering
🔹 Enhance UI with more customization options
🔹 Implement ML-based resume scoring
