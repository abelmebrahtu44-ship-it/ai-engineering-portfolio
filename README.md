# AI Engineering Portfolio

Hands-on, dependency-free Python projects demonstrating practical AI-engineering skills: retrieval-augmented generation, evaluation, workflow safety, and match scoring. Built as a recruiter-friendly portfolio following completion of Scrimba's AI Engineer Path.

## Projects

| Project | Demonstrates | Run |
| --- | --- | --- |
| [Remote AI Job Assistant](./assistant.py) | match scoring, workflow state machines, human approval gates | `python3 assistant.py rank examples/jobs.json` |
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
- Retrieval-augmented generation foundations: chunking, TF-IDF, and cosine similarity
- AI evaluation: structured test cases and repeatable quality checks
- Responsible AI workflows: human approval gates for high-impact actions

## Portfolio roadmap

- Replace the local RAG example with embeddings and a vector database.
- Connect the job assistant to permitted job-board APIs.
- Add LLM-backed response generation and human-reviewed prompt evaluation.
