### To run Ollama with the Phi-3 model completely offline .
 1. Start Ollama
 > ollama serve
 2. Pull the model
 > ollama pull phi3:latest
 3. Run Phi-3 Offline
 > ollama run phi3:latest
 4. Check Downloaded Models
 > ollama list
 5. Run with Custom Prompt
 > ollama run phi3:latest "Explain Kubernetes for beginners"
 6. Stop Ollama
 > CTRL + C
