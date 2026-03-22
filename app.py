from flask import Flask, render_template, request
from utils import extract_text_from_pdf
from nlp import calculate_similarity

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])

def index():
    score = None
    
    if request.method == 'POST':
        file = request.files['resume']
        job_desc = request.form['job_desc']
        
        resume_text = extract_text_from_pdf(file)
        score = calculate_similarity(resume_text,job_desc)
        
        print("Score:", score)
        
    
    return render_template('index.html', score=score)


import os

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
