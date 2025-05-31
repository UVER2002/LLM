from sentence_transformers import SentenceTransformer
import chromadb
from config import QUOTE_FILE, DB_PATH, EMBEDDING_MODEL

encoder = SentenceTransformer(EMBEDDING_MODEL)
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("naheul_rag")

def populate_db():
    with open(QUOTE_FILE) as f:
        quotes = f.read().splitlines()
    embeddings = encoder.encode(quotes)
    collection.add(documents=quotes, embeddings=embeddings.tolist(), ids=[f"id{i}" for i in range(len(quotes))])

def retrieve_context(prompt):
    results = collection.query(query_texts=[prompt], n_results=3)
    return "\n".join(results["documents"][0])
