from .vector_store import (
    create_resume_collection,
    retrieve_relevant_chunks
)

from .rag import generate_rag_analysis


resume = """
I am a Computer Science student with experience in Python,
machine learning, deep learning and computer vision.

I have developed web applications using Flask.

I have experience with SQL, C++, JavaScript and Git.

I have worked on OCR and Vision-Language Models using
PyTorch and LoRA fine-tuning.

I have also developed machine learning projects involving
fraud detection, recommendation systems and NLP.
"""


job_description = """
Software Engineering Intern - Full Stack

We are looking for candidates with strong programming
fundamentals and experience building real projects.

Required skills include Python, JavaScript, React,
Node.js, Express.js, SQL and REST APIs.

Experience with LLMs, embeddings and vector databases
is a plus.
"""


print("Creating vector database...")

collection = create_resume_collection(resume)

print("Vector database created!")

print("\nRetrieving relevant resume sections...")

chunks = retrieve_relevant_chunks(
    collection,
    job_description,
    top_k=5
)

print("Retrieved", len(chunks), "chunks.")

print("\nSending context to Groq LLM...")

analysis = generate_rag_analysis(
    chunks,
    job_description
)

print("\n========== AI ANALYSIS ==========\n")

print("Match Score:", analysis["match_score"])

print("\nMatching Skills:")
for skill in analysis["matching_skills"]:
    print("-", skill)

print("\nMissing Skills:")
for skill in analysis["missing_skills"]:
    print("-", skill)

print("\nRelevant Experience:")
for item in analysis["relevant_experience"]:
    print("-", item)

print("\nSkill Gaps:")
for item in analysis["skill_gaps"]:
    print("-", item)

print("\nRecommendations:")
for item in analysis["recommendations"]:
    print("-", item)