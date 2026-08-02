from pathlib import Path

from pipeline import answer
from retrieval import load_corpus

ROOT = Path(__file__).parent
documents = load_corpus(ROOT / "corpus.jsonl")

for question in [
    "What should a RAG system retrieve before answering?",
    "What is the weather on Mars today?",
]:
    response = answer(question, documents)
    print(f"\nQ: {question}\nA: {response['answer']}\nCitations: {response['citations']}")
