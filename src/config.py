import os
from dotenv import load_dotenv

load_dotenv()

# لا نحتاج OPENAI_API_KEY بعد الآن
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DATA_DIR = "data"
CHROMA_DIR = "chroma_db"
COLLECTION_NAME = "my_knowledge_base"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 100

# ===== Ollama بدل OpenAI =====
EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "qwen2.5:1.5b"       # أو "qwen2.5:7b" للعربية
OLLAMA_BASE_URL = "http://localhost:11434"

TOP_K = 4