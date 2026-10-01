from .vector_store import (
    create_resume_collection,
    retrieve_relevant_chunks
)


resume = """
I am a Computer Science student with experience in Python,
machine learning, deep learning and computer vision.

I have worked with Flask and developed machine learning
applications.

I have experience with SQL, C++, JavaScript and Git.

I have also worked on OCR and Vision-Language Models
using PyTorch and LoRA fine-tuning.
"""


job_description = """
We are looking for a software engineering intern with
Python, machine learning, SQL and backend development
experience.

Experience with AI applications and REST APIs is preferred.
"""


print("Creating vector database...")

collection = create_resume_collection(resume)

print("Vector database created!")

print("\nSearching for relevant resume sections...")

chunks = retrieve_relevant_chunks(
    collection,
    job_description,
    top_k=3
)

print("\nRelevant chunks:\n")

for i, chunk in enumerate(chunks):

    print(f"--- Chunk {i + 1} ---")
    print(chunk)