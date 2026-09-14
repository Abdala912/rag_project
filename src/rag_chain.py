from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.config import LLM_MODEL, OLLAMA_BASE_URL


SYSTEM_PROMPT = """You are an intelligent assistant that answers questions based only on the given context.

Rules:
1. Use only the information found in the context.
2. If you cannot find the answer in the context, say: "I cannot find this information in the available documents."
3. Mention the source (file name) if possible.
4. Answer in the same language as the question.

Context:
{context}
"""


def format_docs(docs):
    formatted = []
    for i, doc in enumerate(docs, 1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page", "")
        header = f"[{i}] source : {source}"
        if page != "":
            header += f" | page: {page}"
        formatted.append(f"{header}\n{doc.page_content}")
    return "\n\n---\n\n".join(formatted)


def build_rag_chain(retriever):
    llm = ChatOllama(
        model=LLM_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=0,
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{question}"),
    ])

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain