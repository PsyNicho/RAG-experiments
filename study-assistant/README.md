# RAG Study Assistant

A RAG-based study assistant that answers questions from study materials using relevant context retrieved from provided documents.

**Status:** In Progress

## How it works

1. Study notes are split into chunks and embedded (all-MiniLM-L6-v2).
2. Embeddings are stored in a custom `VectorIndex` (brute-force cosine search).
3. A question is embedded, the top-k similar chunks are retrieved,
   and they are placed in a prompt for the LLM.
4. The LLM answers only from that context, or says it doesn't know.

## Setup

1. Clone the repo and open the `study-assistant` folder.
2. Create and activate a virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and add your Gemini API key.

## Project structure

- `vector_index.py`: custom vector index
- `test_vector_index.py`: tests for the index
- `test_retrieval.py`: retrieval experiments on a small chunk set (embeds sample chunks, runs test questions, prints top-3 results with scores)
- `docs/retrieval-notes.md`: retrieval experiments and findings

## Progress

- [X] Project setup (virtual environment, dependencies, tests)
- [X] Embeddings with all-MiniLM-L6-v2
- [X] Custom vector index with brute-force cosine search and tests
- [X] Retrieval evaluation on sample study chunks
- [X] LLM selected (Gemini API)
- [ ] Generation: RAG prompt and LLM call
- [ ] End-to-end question answering
- [ ] Document ingestion and chunking from real study material
- [ ] Faster search (approximate index) and benchmark against FAISS
- [ ] Limitations Testing

## LLM choice: Google Gemini API (free tier)

**Decision:** Use the Gemini API via Google AI Studio for generation, targeting `gemini-3.6-flash`.

**Reasons:**

- **Cost:** The free tier is sufficient for development and testing.
- **Capacity:** Expected usage is below the provided daily limits
- **Data consideration:** The indexed material is my own study notes and so sending retrieved chunks to an external API is acceptable.
- **Hardware constraints:** Using hosted inference avoids the performance and memory limitations of my laptop, since it lacks a dedicated GPU.

**Alternative considered:** A local model via Ollama. It is private and works offline, but small models are slow and weaker on this laptop.

**Trade-offs:**

- Needs an internet connection.
- Free-tier limits and available models can change.
- Data handling depends on Google's applicable policies, so  avoid sensitive information.

**Configuration:** The API key is stored in `.env`, which is excluded from Git. `.env.example` documents the required environmental veriable without exposing it.
