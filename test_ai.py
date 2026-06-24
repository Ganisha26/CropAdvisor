from llama_index.llms.ollama import Ollama

# Connect to the local Ollama instance
llm = Ollama(model="phi4-mini", request_timeout=120.0)

# Send a test question
response = llm.complete("What is the best way to test soil nitrogen levels?")

print("--- AI Response ---")
print(response)