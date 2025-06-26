import unittest
from src.tools.dataset_loader import load_arxiv_sample, get_sample_text_and_summary

class TestDatasetLoader(unittest.TestCase):
    def test_load_arxiv_sample(self):
        sample = load_arxiv_sample(1)
        self.assertEqual(len(sample), 1)
        self.assertIn("article", sample[0])
        self.assertIn("abstract", sample[0])

    def test_get_sample_text_and_summary(self):
        text, summary = get_sample_text_and_summary()
        self.assertIsInstance(text, str)
        self.assertIsInstance(summary, str)
        self.assertGreater(len(text), 100)
        self.assertGreater(len(summary), 20)

if __name__ == '__main__':
    unittest.main()