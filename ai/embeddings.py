from fastembed import TextEmbedding

model = TextEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)


def generate_embedding(text):
    """
    Convert a single piece of text into an embedding vector.
    """
    embedding = list(model.embed([text]))[0]
    return embedding.tolist()


def generate_embeddings(texts):
    """
    Convert multiple text chunks into embedding vectors.
    """
    embeddings = model.embed(texts)
    return [embedding.tolist() for embedding in embeddings]