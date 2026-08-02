"""Simple, repeatable quality checks for AI response examples."""
from __future__ import annotations

SAMPLE_OUTPUTS = [
    {
        "name": "grounded-answer",
        "output": "Based on the retrieved context, RAG retrieves relevant passages before generating an answer.",
        "required": ["retrieved context", "retrieves", "before generating"],
    },
    {
        "name": "safe-uncertainty",
        "output": "I do not have enough evidence to confirm that claim, so I would ask for a source.",
        "required": ["enough evidence", "source"],
    },
]


def evaluate(case: dict) -> tuple[bool, list[str]]:
    text = case["output"].lower()
    missing = [phrase for phrase in case["required"] if phrase not in text]
    unsafe = "guaranteed" in text or "definitely true" in text
    issues = ([f"missing: {phrase}" for phrase in missing] + (["unsupported certainty"] if unsafe else []))
    return not issues, issues


if __name__ == "__main__":
    passed = 0
    for case in SAMPLE_OUTPUTS:
        ok, issues = evaluate(case)
        passed += ok
        print(f"{'PASS' if ok else 'FAIL'}  {case['name']}" + (f" — {', '.join(issues)}" if issues else ""))
    print(f"\nPass rate: {passed}/{len(SAMPLE_OUTPUTS)}")
