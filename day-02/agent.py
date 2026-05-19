from langchain_community.llms import Ollama

llm = Ollama(model="phi3")

question = """
You are a DevOps Engineer.

Explain how to troubleshoot:
- Docker container crash
- Kubernetes pod failure
- High CPU issue
"""

response = llm.invoke(question)

print(response)