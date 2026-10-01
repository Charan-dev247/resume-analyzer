import chromadb

from .embeddings import generate_embedding, generate_embeddings


# Persistent ChromaDB database
client = chromadb.PersistentClient(path="chroma_db")


def chunk_text(text, chunk_size=80, overlap=20):
    """
    Split text into overlapping chunks.

    Example:
    chunk 1 -> words 1-100
    chunk 2 -> words 81-180
    chunk 3 -> words 161-260
    """

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def create_resume_collection(resume_text):

    # Split resume into chunks
    chunks = chunk_text(resume_text)

    # Create or reuse collection
    collection = client.get_or_create_collection(
        name="resume_documents"
    )

    # Delete previous documents
    existing = collection.get()

    if existing["ids"]:
        collection.delete(
            ids=existing["ids"]
        )

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Unique ID for every chunk
    ids = [
        f"resume_chunk_{i}"
        for i in range(len(chunks))
    ]

    # Store chunks + embeddings
    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return collection


def retrieve_relevant_chunks(
    collection,
    job_description,
    top_k=5
):

    # Convert job description into embedding
    job_embedding = generate_embedding(
        job_description
    )

    # Search vector database
    results = collection.query(
        query_embeddings=[job_embedding],
        n_results=top_k
    )

    return results["documents"][0]