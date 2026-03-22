<img width="1220" height="483" alt="image" src="https://github.com/user-attachments/assets/2282bb4f-1ae5-4112-b50e-43d8943217df" />

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

## 📂 Project Structure
