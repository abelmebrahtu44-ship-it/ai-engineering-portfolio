"""Dependency-free TF-IDF retrieval component for a small RAG prototype."""
import math, re, sys
from collections import Counter

DOCUMENTS = [
    "RAG retrieves relevant source passages before a language model writes an answer.",
    "Chunking splits long documents into focused passages for retrieval.",
    "Evaluation should test relevance, groundedness, and evidence support.",
]

def tokens(text):
    return re.findall(r"[a-z]{2,}", text.lower())

def vector(text):
    words = tokens(text); counts = Counter(words); total = len(words) or 1
    return {word: (count / total) * math.log((len(DOCUMENTS)+1)/(1+sum(word in tokens(doc) for doc in DOCUMENTS))+1) for word, count in counts.items()}

def cosine(a, b):
    numerator = sum(value * b.get(word, 0) for word, value in a.items())
    size = math.sqrt(sum(x*x for x in a.values())) * math.sqrt(sum(x*x for x in b.values()))
    return numerator / size if size else 0

def retrieve(question, limit=2):
    query = vector(question)
    return sorted([(cosine(query, vector(doc)), doc) for doc in DOCUMENTS], reverse=True)[:limit]

question = " ".join(sys.argv[1:]) or "How should I evaluate a RAG system?"
for score, passage in retrieve(question):
    print(f"[{score:.3f}] {passage}")
