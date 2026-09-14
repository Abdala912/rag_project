from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from src.config import (
    CHROMA_DIR,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    OLLAMA_BASE_URL,
)


def get_embedding_model():
    return OllamaEmbeddings(
        model=EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


def build_vectorstore(chunks, reset: bool = False):
    embedding = get_embedding_model()

    if reset:
        import shutil, os
        if os.path.exists(CHROMA_DIR):
            shutil.rmtree(CHROMA_DIR)
            print("[RESET] The old database has been deleted.")

    print("[EMBED] embedding to ChromaDB...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_DIR,
    )
    print(f"[OK] stored {len(chunks)} chunk in ChromaDB")
    return vectorstore


def load_vectorstore():
    embedding = get_embedding_model()
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding,
        persist_directory=CHROMA_DIR,
    )