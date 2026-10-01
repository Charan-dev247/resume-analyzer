from embeddings import generate_embedding


text = "I am a machine learning engineer with Python experience."

embedding = generate_embedding(text)

print("Embedding generated successfully!")
print("Number of dimensions:", len(embedding))
print("First 5 values:", embedding[:5])