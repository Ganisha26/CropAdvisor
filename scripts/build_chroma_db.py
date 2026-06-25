from sentence_transformers import SentenceTransformer
import chromadb
import os

chunks = []

# Read all txt files from data folder
for filename in os.listdir("data"):
    if filename.endswith(".txt"):
        filepath = os.path.join("data", filename)

        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    chunks.append(line)

print(f"Loaded {len(chunks)} chunks")

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Chroma client
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_or_create_collection("agri_knowledge")

# Clear old entries
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