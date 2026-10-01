# Python, Machine Learning & AI Learning Journey

A hands-on learning repository covering Python fundamentals, data structures and algorithms, data analysis, Machine Learning, Deep Learning, NLP, Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and AI Agents.

## Goals
- Build strong Python fundamentals and clean coding habits.
- Practice data structures, algorithms, and testing.
- Learn NumPy, Pandas, visualization, statistics, and ML.
- Build and evaluate practical ML and AI projects.
- Learn LLM application patterns, RAG, tool calling, and agent safety.
- Track progress through code, experiments, and learning notes.

## Roadmap
1. **Python fundamentals** — types, conditions, loops, functions, collections, modules, exceptions, files, OOP, type hints, testing.
2. **DSA** — arrays, strings, hash maps, stacks, queues, linked lists, sorting, searching, recursion, trees, heaps, graphs, complexity.
3. **Data analysis** — NumPy, Pandas, Matplotlib, data cleaning, exploratory analysis.
4. **Math and statistics** — linear algebra, probability, distributions, derivatives, gradient descent.
5. **Machine Learning** — regression, classification, clustering, feature engineering, cross-validation, model evaluation.
6. **Deep Learning** — neural networks, backpropagation, optimizers, CNNs, PyTorch.
7. **NLP and Transformers** — preprocessing, tokenization, embeddings, attention, pretrained models.
8. **LLMs and prompting** — model APIs, prompt design, structured outputs, evaluation, privacy and safety.
9. **Embeddings and vector search** — semantic similarity, indexing, retrieval, metadata filtering.
10. **RAG** — document loading, chunking, retrieval, grounded answers, citations, evaluation.
11. **AI Agents** — tool calling, state, workflows, human approval, guardrails, evaluation, multi-agent patterns.

## Repository structure
```text
MachineLearning/
├── README.md
├── .gitignore
├── requirements.txt
├── pyproject.toml
├── src/python_ai_learning/   # reusable Python package
├── tests/                    # automated tests
├── notebooks/                # Jupyter notebooks
├── learning/                 # topic-wise exercises and notes
├── projects/                 # end-to-end portfolio projects
└── docs/                     # learning log
```

## Setup with VS Code
Recommended: Python 3.12+, Git, and VS Code with the Python extension.

Create and activate a virtual environment from the repository root:

```bash
python -m venv .venv
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

Install the project and dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e .
python -m pip install -r requirements.txt
```

Run the starter application and tests:

```bash
python -m python_ai_learning.main
python -m pytest -v
```

## Projects to build
- Python CLI learning tracker
- Exploratory data analysis and visualization
- Supervised ML prediction pipeline
- Image classifier
- Document question-answering RAG system
- AI agent with controlled tool access and evaluation

## Progress tracking
Use `docs/learning-log.md` to record weekly topics, exercises, problems solved, and next steps. Add small, tested commits as you learn.

## Safe and reproducible work
- Never commit API keys, passwords, tokens, private datasets, or local `.env` files.
- Document dataset sources and licensing.
- Keep large datasets and model artifacts out of normal Git history.
- Evaluate model quality, limitations, privacy, and safety before sharing demos.
