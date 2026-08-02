"""Evaluate answerability, citation validity, and abstention precision."""
from __future__ import annotations

import json
from pathlib import Path

from pipeline import answer, citation_is_valid
from retrieval import load_corpus

ROOT = Path(__file__).parent
documents = load_corpus(ROOT / "corpus.jsonl")
cases = [json.loads(line) for line in (ROOT / "evals.jsonl").read_text().splitlines() if line.strip()]

answerability = citations = abstention_hits = abstention_total = 0
for case in cases:
    response = answer(case["question"], documents)
    answerability += response["abstained"] == (not case["answerable"])
    citations += citation_is_valid(response) and (not case["answerable"] or case["expected_source"] in response["citations"])
    if response["abstained"]:
        abstention_total += 1
        abstention_hits += not case["answerable"]

total = len(cases)
print(json.dumps({
    "cases": total,
    "answerability_accuracy": round(answerability / total, 2),
    "citation_validity": round(citations / total, 2),
    "abstention_precision": round(abstention_hits / abstention_total, 2) if abstention_total else None,
}, indent=2))
