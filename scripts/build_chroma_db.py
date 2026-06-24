from sentence_transformers import SentenceTransformer
import chromadb

# Read knowledge file
with open("data/agri_knowledge.txt", "r", encoding="utf-8") as f:
    chunks = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(chunks)} chunks")

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Chroma client
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_or_create_collection("agri_knowledge")

# Clear old entries if any
try:
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])
except:
    pass

# Add chunks
for i, chunk in enumerate(chunks):
    embedding = model.encode(chunk).tolist()

    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("✅ Vector database created successfully")