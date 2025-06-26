import unittest
from src.graph.executor import run_rag_pipeline
import os

class TestGraph(unittest.TestCase):
    def test_rag_pipeline_output(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.skipTest("API key not set")

        document = """Dropout is a regularization technique for neural networks that prevents overfitting.
        It works by randomly dropping units during training."""
        query = "What is dropout?"
        response = run_rag_pipeline(query, document, api_key)
        self.assertTrue("dropout" in response.lower())

if __name__ == '__main__':
    unittest.main()