from flask import Flask, render_template, request, jsonify

from utils import extract_text_from_pdf
from nlp import calculate_similarity

from ai.vector_store import (
    create_resume_collection,
    retrieve_relevant_chunks
)

from ai.rag import generate_rag_analysis


app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def health():
    return {
        "status": "ok",
        "service": "resume-intelligence-ai"
    }


@app.route('/', methods=['GET', 'POST'])
def index():

    score = None
    analysis = None
    error = None

    if request.method == 'POST':

        try:
            # Get uploaded resume
            file = request.files.get('resume')

            # Get job description
            job_desc = request.form.get('job_desc', '').strip()

            # Basic validation
            if not file:
                error = "Please upload a resume PDF."

            elif not job_desc:
                error = "Please enter a job description."

            else:

                # ==========================================
                # 1. Extract text from resume PDF
                # ==========================================

                resume_text = extract_text_from_pdf(file)

                if not resume_text.strip():
                    error = "Could not extract text from the PDF."

                else:

                    # ==========================================
                    # 2. Traditional TF-IDF similarity
                    # ==========================================

                    score = calculate_similarity(
                        resume_text,
                        job_desc
                    )

                    print("TF-IDF Score:", score)


                    # ==========================================
                    # 3. Create vector database
                    # ==========================================

                    collection = create_resume_collection(
                        resume_text
                    )


                    # ==========================================
                    # 4. Retrieve relevant resume chunks
                    # ==========================================

                    relevant_chunks = retrieve_relevant_chunks(
                        collection,
                        job_desc,
                        top_k=5
                    )

                    print(
                        "Retrieved chunks:",
                        len(relevant_chunks)
                    )


                    # ==========================================
                    # 5. RAG + LLM analysis
                    # ==========================================

                    analysis = generate_rag_analysis(
                        relevant_chunks,
                        job_desc
                    )

                    print("RAG Analysis:", analysis)

        except Exception as e:

            print("ERROR:", e)

            error = f"Something went wrong: {str(e)}"


    return render_template(
        'index.html',
        score=score,
        analysis=analysis,
        error=error
    )


import os

@app.route('/api/analyze', methods=['POST'])
def analyze_api():
    try:
        file = request.files.get('resume')
        job_desc = request.form.get('job_desc', '').strip()

        if not file:
            return jsonify({"error": "Resume PDF is required"}), 400

        if not job_desc:
            return jsonify({"error": "Job description is required"}), 400

        resume_text = extract_text_from_pdf(file)

        if not resume_text.strip():
            return jsonify({"error": "Could not extract text from PDF"}), 400

        # Traditional TF-IDF
        score = calculate_similarity(resume_text, job_desc)

        # RAG
        collection = create_resume_collection(resume_text)

        relevant_chunks = retrieve_relevant_chunks(
            collection,
            job_desc,
            top_k=5
        )

        analysis = generate_rag_analysis(
            relevant_chunks,
            job_desc
        )

        return jsonify({
            "tfidf_score": score,
            "rag_analysis": analysis
        })

    except Exception as e:
        print("API ERROR:", e)
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=int(
            os.environ.get("PORT", 10000)
        )
    )