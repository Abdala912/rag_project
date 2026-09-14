# 🤖 RAG Project

A complete Retrieval-Augmented Generation (RAG) system built with LangChain, ChromaDB, and Ollama.

## ✨ Features

- 📄 Supports PDF and TXT documents
- 🔍 Semantic search with ChromaDB
- 🦙 Local models via Ollama (100% free)
- 🌍 Multilingual support (including Arabic)
- 📚 Displays sources alongside each answer
- ⚡ Fast and fully private (works offline)

## 🏗️ Project Structure

```
rag_project/
├── data/                    # Documents (PDF/TXT)
├── src/
│   ├── config.py            # Configuration
│   ├── loader.py            # Document loading
│   ├── splitter.py          # Text chunking
│   ├── vectorstore.py       # ChromaDB integration
│   ├── retriever.py         # Retrieval logic
│   └── rag_chain.py         # RAG chain
├── ingest.py                # Build vector database
├── query.py                 # CLI query interface
├── requirements.txt
└── README.md
```

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag_project.git
cd rag_project
```

### 2. Create a conda environment

```bash
conda create -n rag_env python=3.11 -y
conda activate rag_env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download from [ollama.com/download](https://ollama.com/download), then pull the models:

```bash
ollama pull qwen2.5:1.5b
ollama pull nomic-embed-text
```

## 📖 Usage

### 1. Add your documents to `data/`

```bash
cp your_document.pdf data/
```

### 2. Build the vector database

```bash
python ingest.py --reset
```

### 3. Ask questions

```bash
python query.py
```

## ⚙️ Configuration

Edit `src/config.py`:

| Variable | Description | Default |
|----------|-------------|---------|
| `CHUNK_SIZE` | Size of each text chunk | 800 |
| `CHUNK_OVERLAP` | Overlap between chunks | 100 |
| `EMBEDDING_MODEL` | Embedding model | `nomic-embed-text` |
| `LLM_MODEL` | LLM for generation | `qwen2.5:1.5b` |
| `TOP_K` | Number of retrieved chunks | 4 |

## 🛠️ Technologies

- [LangChain](https://python.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [Ollama](https://ollama.com/)
- [Python 3.11+](https://www.python.org/)

## 📝 License

MIT License