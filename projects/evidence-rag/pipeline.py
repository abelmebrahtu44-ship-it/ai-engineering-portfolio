"""Grounded response contract with citation and abstention behavior."""
from __future__ import annotations

from retrieval import retrieve

MIN_RELEVANCE = 0.08


def answer(question: str, documents: list[dict]) -> dict:
    evidence = retrieve(question, documents, limit=2)
    best = evidence[0]
    if best["score"] < MIN_RELEVANCE:
        return {
            "answer": "I do not have enough evidence in the available sources to answer that.",
            "citations": [],
            "abstained": True,
            "evidence": evidence,
        }
    return {
        "answer": f"Based on the available evidence: {best['text']}",
        "citations": [best["id"]],
        "abstained": False,
        "evidence": evidence,
    }


def citation_is_valid(response: dict) -> bool:
    evidence_ids = {item["id"] for item in response["evidence"]}
    return response["abstained"] or bool(response["citations"]) and set(response["citations"]) <= evidence_ids
