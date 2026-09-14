import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

from src.vectorstore import load_vectorstore
from src.retriever import get_retriever
from src.rag_chain import build_rag_chain


def main():
    print("=" * 50)
    print("[READY] RAG system is ready — type 'exit' to quit")
    print("=" * 50)

    vectorstore = load_vectorstore()
    retriever = get_retriever(vectorstore)
    chain = build_rag_chain(retriever)

    while True:
        question = input("\n[?] your Question:  ").strip()

        if question in ["خروج", "exit", "quit"]:
            print("Bye!")
            break

        if not question:
            continue

        print("\n[...] Searching..\n")
        answer = chain.invoke(question)
        print(f"[ANSWER]\n{answer}")


if __name__ == "__main__":
    main()