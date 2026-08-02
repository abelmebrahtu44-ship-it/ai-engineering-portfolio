"""A dependency-free retrieval component for a small RAG prototype."""
from __future__ import annotations

import math
import re
import sys
from collections import Counter

DOCUMENTS = [
    "RAG systems retrieve relevant source passages before a language model writes an answer.",
    "Chunking splits long documents into smaller passages so a retriever can return focused context.",
    "Evaluation should test relevance, groundedness, and whether an answer is supported by retrieved evidence.",
    "Human review is important when AI output influences job applications or other high-impact decisions."
]


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z]{2,}", text.lower())


def vector(text: str, corpus: list[str]) -> dict[str, float]:
    words = tokens(text)
    counts = Counter(words)
    total = len(words) or 1
    return {
        word: (count / total) * math.log((len(corpus) + 1) / (1 + sum(word in tokens(doc) for doc in corpus)) + 1)
        for word, count in counts.items()
    }


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    numerator = sum(value * right.get(word, 0) for word, value in left.items())
    magnitude = math.sqrt(sum(value * value for value in left.values())) * math.sqrt(sum(value * value for value in right.values()))
    return numerator / magnitude if magnitude else 0.0


def retrieve(question: str, limit: int = 2):
    query = vector(question, DOCUMENTS)
    scored = [(cosine(query, vector(document, DOCUMENTS)), document) for document in DOCUMENTS]
    return sorted(scored, reverse=True)[:limit]


if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "How should I evaluate a RAG system?"
    print(f"Question: {question}\n\nRetrieved context:")
    for score, passage in retrieve(question):
        print(f"- [{score:.3f}] {passage}")
