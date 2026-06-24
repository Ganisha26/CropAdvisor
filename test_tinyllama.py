from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="tinyllama",
    request_timeout=120.0
)

response = llm.complete("Reply with exactly: WORKING")

print(response)