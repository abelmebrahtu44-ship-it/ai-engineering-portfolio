"""Deterministic retrieval primitives for an evidence-grounded RAG prototype."""
from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path


def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z]{2,}", text.lower())


def load_corpus(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def vector(text: str, documents: list[dict]) -> dict[str, float]:
    words = tokenize(text)
    counts = Counter(words)
    total = len(words) or 1
    return {
        word: (count / total) * math.log((len(documents) + 1) / (1 + sum(word in tokenize(doc["text"]) for doc in documents)) + 1)
        for word, count in counts.items()
    }


def cosine(left: dict[str, float], right: dict[str, float]) -> float:
    numerator = sum(weight * right.get(term, 0) for term, weight in left.items())
    magnitude = math.sqrt(sum(weight * weight for weight in left.values())) * math.sqrt(sum(weight * weight for weight in right.values()))
    return numerator / magnitude if magnitude else 0.0


def retrieve(question: str, documents: list[dict], limit: int = 2) -> list[dict]:
    query = vector(question, documents)
    ranked = []
    for document in documents:
        score = cosine(query, vector(document["text"], documents))
        ranked.append({**document, "score": score})
    return sorted(ranked, key=lambda item: item["score"], reverse=True)[:limit]
