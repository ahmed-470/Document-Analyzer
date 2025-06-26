from typing import List
import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

def embed_query(query: str, api_key: str) -> List[float]:
    client = OpenAI(api_key=api_key)
    response = client.embeddings.create(
        input=[query],
        model="text-embedding-ada-002"
    )
    return response.data[0].embedding

def retrieve_top_chunks(query: str, chunks: List[str], embeddings: List[List[float]], api_key: str, top_k: int = 5) -> List[str]:
    query_embedding = embed_query(query, api_key)
    scores = cosine_similarity([query_embedding], embeddings)[0]
    top_indices = scores.argsort()[-top_k:][::-1]
    return [chunks[i] for i in top_indices]