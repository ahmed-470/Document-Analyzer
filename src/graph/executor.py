from src.nodes.rag_node import RAGNode

rag_node = RAGNode()

def run_rag_pipeline(query: str, document: str, api_key: str) -> str:
    """
    Executes the RAG pipeline: embeds document, retrieves relevant chunks,
    and generates response using the LLM.
    """
    return rag_node.process(query, document, api_key)