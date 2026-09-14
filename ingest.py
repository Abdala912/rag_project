import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import build_vectorstore


def main():
    print("=" * 50)
    print("[START] starting the process")
    print("=" * 50)

    documents = load_documents("data")
    chunks = split_documents(documents)
    build_vectorstore(chunks, reset=True)

    print("\n[SUCCESS] the process has completed")


if __name__ == "__main__":
    main()