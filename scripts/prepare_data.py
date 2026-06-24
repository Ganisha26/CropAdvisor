# Improved chunking for RAG system

file_path = "data/agri_knowledge.txt"

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Step 1: split by new lines first
lines = text.split("\n")

# Step 2: clean bullets and empty lines
chunks = []
for line in lines:
    line = line.strip()
    if line.startswith("-"):
        line = line[1:].strip()
    if len(line) > 0:
        chunks.append(line)

print("Total chunks created:", len(chunks))
print("\nClean chunks:")
for c in chunks:
    print("-", c)