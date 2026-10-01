from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embedding(text):
    """
    Convert a single piece of text into an embedding vector.
    """
    return model.encode(text).tolist()


def generate_embeddings(texts):
    """
    Convert multiple text chunks into embedding vectors.
    """
    return model.encode(texts).tolist()