from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader

LOADERS = {
    ".pdf": PyPDFLoader,
    ".txt": TextLoader,
}


def load_documents(data_dir: str = "data"):
    documents = []
    data_path = Path(data_dir)

    if not data_path.exists():
        raise FileNotFoundError(f"المجلد غير موجود: {data_dir}")

    for file_path in data_path.iterdir():
        if file_path.is_dir():
            continue

        suffix = file_path.suffix.lower()
        loader_cls = LOADERS.get(suffix)

        if loader_cls is None:
            print(f"[SKIP] صيغة غير مدعومة: {file_path.name}")
            continue

        print(f"[LOAD] {file_path.name}")
        loader = loader_cls(str(file_path))
        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = file_path.name

        documents.extend(docs)

    print(f"[OK] تم تحميل {len(documents)} صفحة/مستند")
    return documents