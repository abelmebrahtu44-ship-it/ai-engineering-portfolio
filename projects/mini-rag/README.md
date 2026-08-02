# Mini RAG Retriever

A transparent retrieval-augmented-generation building block implemented from scratch. It chunks a small knowledge base, calculates TF-IDF vectors, and returns the most relevant passages for a question.

```bash
python3 app.py "What should a RAG system do before generating an answer?"
```

This project intentionally stops at retrieval: an LLM can use the returned passages as grounded context in a later integration.
