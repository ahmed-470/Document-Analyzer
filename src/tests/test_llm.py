import unittest
from src.llm.openai_client import query_openai
import os

class TestLLM(unittest.TestCase):
    def test_query_openai_format(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            self.skipTest("API key not set")
        prompt = "Say hello"
        response = query_openai(prompt, api_key)
        self.assertTrue(isinstance(response, str))
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()