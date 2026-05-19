from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi3")

response = llm.invoke("Explain Git in simple words")

print("\nAI Response:\n")
print(response)
