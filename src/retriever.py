from src.config import TOP_K


def get_retriever(vectorstore, top_k: int = TOP_K):
    return vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": top_k},
    )