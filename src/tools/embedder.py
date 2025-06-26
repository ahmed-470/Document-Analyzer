from openai import OpenAI
from typing import List

def get_embeddings(chunks: List[str], api_key: str) -> List[List[float]]:
    client = OpenAI(api_key=api_key)
    try:
        response = client.embeddings.create(
            input=chunks,
            model="text-embedding-ada-002"
        )
        return [e.embedding for e in response.data]
    except Exception as e:
        raise RuntimeError(f"Embedding error: {e}")