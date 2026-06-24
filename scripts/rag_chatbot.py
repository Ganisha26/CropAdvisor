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
        n_results=1
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are a retrieval assistant.

Use ONLY the information provided in the context.

Do NOT add any extra information.

If the answer is not present in the context, reply:
"I don't have enough information in my knowledge base."

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

    print("\nAnswer:")
    print(results["documents"][0][0])