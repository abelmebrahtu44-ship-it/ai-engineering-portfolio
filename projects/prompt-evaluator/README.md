# Prompt Evaluation Harness

A small example of turning prompt quality into repeatable tests. The evaluator checks local sample outputs for required concepts and flags unsupported certainty claims.

```bash
python3 app.py
```

In production, replace `SAMPLE_OUTPUTS` with calls to a model and expand the test suite with domain-specific cases.
