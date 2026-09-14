from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ". ", "؟ ", "! ", "، ", " "],
    )

    chunks = splitter.split_documents(documents)
    print(f"[OK] Created {len(chunks)} chunk(s)")
    return chunks