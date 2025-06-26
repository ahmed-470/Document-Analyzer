import unittest
import os
from src.tools.embedder import get_embeddings
from src.tools.retriever import retrieve_top_chunks

class TestTools(unittest.TestCase):
    def setUp(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            self.skipTest("API key not set")
        self.chunks = [
            "Dropout is used in deep learning.",
            "Gradient descent is an optimization method.",
            "Overfitting is common in neural networks."
        ]

    def test_embeddings_and_retrieval(self):
        embeddings = get_embeddings(self.chunks, self.api_key)
        self.assertEqual(len(embeddings), len(self.chunks))

        query = "What is dropout?"
        top_chunks = retrieve_top_chunks(query, self.chunks, embeddings, self.api_key)
        self.assertTrue(any("dropout" in c.lower() for c in top_chunks))

if __name__ == '__main__':
    unittest.main()