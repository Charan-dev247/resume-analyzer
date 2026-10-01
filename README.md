<<<<<<< HEAD

# 🚀 AI Resume Analyzer (NLP)

A web-based application that analyzes resumes against job descriptions using Natural Language Processing (NLP) techniques.

🌐 **Live Demo:**  
👉 https://resume-analyzer-tmez.onrender.com/

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 📝 Paste Job Description
- 📊 Computes Match Score (%)
- 🧠 TF-IDF based text vectorization
- 📐 Cosine similarity for comparison
- 🎨 Clean and responsive UI
- 🌐 Deployed live on Render

---

## 🧠 How It Works

1. Extracts text from uploaded resume (PDF)  
2. Cleans and preprocesses text (lowercasing, regex cleaning)  
3. Converts text into vectors using TF-IDF  
4. Computes similarity using cosine similarity  
5. Displays match score  

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)  
- **NLP:** Scikit-learn (TF-IDF, Cosine Similarity)  
- **Frontend:** HTML, CSS  
- **Libraries:** PyPDF2, NumPy  
- **Deployment:** Render  

---

## 📂 Project Structure
resume-analyzer/
│
├── app.py # Flask backend
├── nlp.py # NLP processing (TF-IDF + similarity)
├── utils.py # PDF text extraction
├── requirements.txt # Dependencies
├── Procfile # Deployment config
│
├── static/
│ └── style.css # Styling
│
└── templates/
└── index.html # UI


---

## ⚙️ Run Locally

```bash
git clone https://github.com/YOUR-USERNAME/resume-analyzer-nlp.git
cd resume-analyzer-nlp
pip install -r requirements.txt
python app.py
```

## ⚠️ Design Decisions

- Removed lemmatization to avoid dependency issues in deployment (NLTK WordNet not available in production environment)
- Used TF-IDF for efficient and lightweight text vectorization
- Prioritized system stability, simplicity, and deployability over minor accuracy improvements

## 🚀 Future Improvements

- 🔍 Missing skills extraction
- 📊 Keyword highlighting
- 📈 Resume score breakdown
- 🤖 Use advanced NLP models (Word2Vec, BERT)
- 📄 Support additional file formats (DOCX, TXT)
- 🎯 Provide resume improvement suggestions

## 👤 Author

**Suluru Charan Sai**  

📧 Email: sulurucharan@gmail.com  
🌐 GitHub: https://github.com/Charan-dev247  
💼 LinkedIn: https://linkedin.com/in/suluru-charan-sai-4b33a6323  
=======
# AI Resume Intelligence

An AI-powered resume analysis platform that compares a candidate's resume with a job description using traditional TF-IDF similarity and a Retrieval-Augmented Generation (RAG) pipeline.

## Features

- Resume PDF text extraction
- Traditional TF-IDF keyword similarity
- Text chunking
- Semantic embeddings using Sentence Transformers
- ChromaDB vector database
- Semantic retrieval of relevant resume sections
- LLM-powered resume analysis
- Matching skills identification
- Missing skills detection
- Skill-gap analysis
- Relevant experience extraction
- Personalized recommendations
- React frontend
- Node.js + Express REST API
- Python Flask AI backend

## Architecture

React Frontend
       |
       v
Node.js + Express REST API
       |
       v
Python Flask AI Backend
       |
       +----------------------+
       |                      |
       v                      v
TF-IDF Similarity       RAG Pipeline
                              |
                              v
                     Text Chunking
                              |
                              v
                     Sentence Embeddings
                              |
                              v
                         ChromaDB
                              |
                              v
                       Relevant Chunks
                              |
                              v
                           Groq LLM
                              |
                              v
                       Structured Analysis

## Tech Stack

### Frontend
- React
- Vite
- HTML
- CSS
- JavaScript

### Backend
- Node.js
- Express.js
- REST APIs
- Python
- Flask

### AI / NLP
- Sentence Transformers
- Embeddings
- Retrieval-Augmented Generation (RAG)
- TF-IDF
- Cosine Similarity
- Large Language Models

### Database
- ChromaDB

## How It Works

1. User uploads a resume PDF.
2. User provides a job description.
3. The React frontend sends the data to the Node.js/Express API.
4. Express forwards the request to the Flask AI backend.
5. The resume text is extracted from the PDF.
6. TF-IDF similarity is calculated as a traditional keyword-based baseline.
7. The resume is divided into text chunks.
8. Each chunk is converted into an embedding.
9. Embeddings are stored in ChromaDB.
10. The job description is converted into an embedding.
11. ChromaDB retrieves the most relevant resume sections.
12. The retrieved context is sent to an LLM.
13. The LLM generates structured resume-job analysis.
14. Results are returned to the React frontend.

## AI Analysis

The system generates:

- AI match score
- Matching skills
- Missing skills
- Relevant experience
- Skill gaps
- Recommendations

The application also displays the traditional TF-IDF similarity alongside the RAG-based analysis to demonstrate the difference between lexical matching and semantic analysis.

## Running Locally

### Python backend

Install dependencies:

```bash
pip install -r requirements.txt
>>>>>>> 4901116 (Build AI resume intelligence full stack pipeline)
