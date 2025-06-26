from src.tools.embedder import get_embeddings
from src.tools.retriever import retrieve_top_chunks
from src.llm.openai_client import query_openai

class RAGNode:
    def __init__(self, top_k: int = 5):
        self.top_k = top_k

    def process(self, query: str, document: str, api_key: str) -> str:
        chunks = document.split("\n\n")  # Simple paragraph chunking
        embeddings = get_embeddings(chunks, api_key)
        relevant_chunks = retrieve_top_chunks(query, chunks, embeddings, api_key, self.top_k)
        context = "\n\n".join(relevant_chunks)

        prompt = (
            f"You are an expert assistant. Based on the context below, answer the query.\n"
            f"\nContext:\n{context}\n\nQuery: {query}\nAnswer:"
        )

        return query_openai(prompt, api_key)