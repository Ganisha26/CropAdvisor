from sentence_transformers import SentenceTransformer
import chromadb
import subprocess

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="vector_db")
collection = client.get_collection("agri_knowledge")

while True:
    query = input("\nAsk a question (or type 'exit'): ")

    if query.lower() == "exit":
        break

    # Retrieve relevant knowledge
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an agricultural assistant.

Rules:
1. Use ONLY the provided context.
2. Answer in 1-2 sentences.
3. Do not repeat information.
4. Do not add information not present in context.
5. Be concise and factual.

Context:
{context}

Question:
{query}

Answer:
"""
response = subprocess.run(
    ["ollama", "run", "tinyllama"],
    input=prompt,
    text=True,
    capture_output=True,
    encoding="utf-8",
    errors="ignore"
)

answer = response.stdout.strip().split("Answer:")[-1].strip()

print("\nAnswer:")
print(answer)

response = subprocess.run(
    ["ollama", "run", "tinyllama"],
    input=prompt,
    text=True,
    capture_output=True,
    encoding="utf-8",
    errors="ignore"

    )

print("\nAnswer:")
    
print(response.stdout)
