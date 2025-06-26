from datasets import load_dataset

def load_arxiv_sample(n: int = 1):
    """
    Loads n samples from the arXiv summarization dataset.
    """
    dataset = load_dataset("ccdv/arxiv-summarization", split="test")
    return dataset.select(range(n))

def get_sample_text_and_summary(index=0):
    """
    Returns one document and its summary from the dataset.
    """
    sample = load_arxiv_sample(n=index+1)[index]
    return sample['article'], sample['abstract']