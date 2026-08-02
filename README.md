# AI Engineering Portfolio

Practical Python projects demonstrating AI-engineering fundamentals: retrieval-augmented generation, evaluation, workflow safety, and match scoring. Built after completing Scrimba's AI Engineer Path.

## What I’m demonstrating

- Building grounded retrieval pipelines instead of relying on unsupported model claims
- Evaluating AI behavior with repeatable, versioned test cases
- Designing human approval gates for high-impact AI workflows
- Writing clear, runnable code with automated checks

## Projects

| Project | Demonstrates | Run |
| --- | --- | --- |
| [Remote AI Job Assistant](./assistant.py) | match scoring, workflow state machines, human approval gates | `python3 assistant.py rank examples/jobs.json` |
| [Evidence RAG Workbench](./projects/evidence-rag) | retrieval, citation validation, abstention, evaluation metrics, unit tests | `python3 -m unittest discover -s projects/evidence-rag/tests` |
| [Mini RAG Retriever](./projects/mini-rag) | document chunking, TF-IDF retrieval, cosine similarity | `python3 projects/mini-rag/app.py "How do I prepare for an AI interview?"` |
| [Prompt Evaluation Harness](./projects/prompt-evaluator) | structured test cases, automated quality checks, pass-rate reporting | `python3 projects/prompt-evaluator/app.py` |

## Setup

Python 3.10+ is the only requirement. Each project runs entirely locally with no API keys or third-party packages.

## Remote AI Job Assistant

An approval-first job-search workflow that ranks junior and senior remote AI openings against an editable candidate profile. It keeps personal application history in the ignored `data/` directory and prevents an application from being marked submitted until you explicitly approve it.

```bash
python3 assistant.py rank examples/jobs.json
python3 assistant.py add-example
python3 assistant.py approve 1
python3 assistant.py submit 1
```

Edit [`config/profile.json`](config/profile.json) with only skills and experience you can substantiate.

## Skills demonstrated

- Python application development and command-line tooling
- Retrieval-augmented generation foundations: chunking, lexical retrieval, and cosine similarity
- AI evaluation: structured test cases, citation checks, and repeatable metrics
- Responsible AI workflows: human approval gates for high-impact actions
- Test automation through GitHub Actions

## Running the flagship project

```bash
cd projects/evidence-rag
python3 demo.py
python3 evaluate.py
python3 -m unittest discover -s tests -v
```

The workbench is intentionally dependency-free so the retrieval and evaluation logic is inspectable. Its design makes it straightforward to replace lexical ranking with embeddings and connect a hosted model later.

## Portfolio roadmap

- Replace the local RAG example with embeddings and a vector database.
- Connect the job assistant to permitted job-board APIs.
- Add LLM-backed response generation and human-reviewed prompt evaluation.
