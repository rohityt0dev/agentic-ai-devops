# 🚀 AI + DevOps Foundations — Day 1

<p align="center">
  <img src="https://img.shields.io/badge/AI-DevOps-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Docker-Containerization-blue?style=for-the-badge&logo=docker">
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge">
  <img src="https://img.shields.io/badge/LangChain-AI%20Framework-green?style=for-the-badge">
</p>

---

# 📌 Introduction

Introduces the fundamentals of **AI + DevOps Engineering** and helps beginners set up a complete local AI development environment.

## 🎯 What You Will Learn

- What Artificial Intelligence is
- Traditional AI vs Generative AI
- AI Agents and their components
- Real-world AI use cases in DevOps
- Running local LLMs using Ollama
- Building your first AI-powered DevOps assistant using Python and LangChain

---

# 🏗️ Architecture

```text
                +----------------------+
                |      User Prompt     |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      Python App      |
                |    (LangChain)       |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |       Ollama         |
                |   Local LLM Server   |
                +----------+-----------+
                           |
                           v
                +----------------------+
                |      Phi-3 Model     |
                +----------------------+
```

---

# 🤖 What is AI?

Artificial Intelligence (AI) is a branch of computer science focused on building systems capable of performing tasks that normally require human intelligence.

### Examples

- Learning
- Problem-solving
- Decision-making
- Understanding language
- Visual recognition

---

# ⚡ Traditional AI vs Generative AI

| Feature | Traditional AI | Generative AI |
|----------|----------------|----------------|
| Primary Function | Analytical tasks | Creates new content |
| Output | Predictions & decisions | Text, images, code |
| Examples | Spam filters, fraud detection | ChatGPT, image generation |
| Technology | ML algorithms | Transformers, GANs |
| Data Usage | Analyzes existing data | Generates new data |
| Adaptability | Limited retraining | Learns from large datasets |

---

# 🧠 What is an AI Agent?

An AI Agent is a system capable of reasoning, planning, and taking actions autonomously.

| Component | Purpose |
|------------|----------|
| LLM | Brain |
| Memory | Stores context |
| Tools | Executes actions |
| Planning | Decides next steps |
| Orchestrator | Manages workflow |

---

# 💡 Real DevOps AI Use Cases

| Use Case | Example |
|-----------|----------|
| Incident Response | AI analyzes alerts |
| Kubernetes Troubleshooting | Detects pod failures |
| CI/CD Automation | Generates pipelines |
| Cloud Optimization | Reduces AWS cost |
| Security Scanning | Detects vulnerabilities |
| Monitoring | Predicts failures |

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | AI application development |
| Ollama | Run local LLMs |
| LangChain | AI orchestration |
| Docker | Containerization |
| Git | Version control |
| VS Code | Code editor |

---

# ✨ Features

- ✅ Local AI setup using Ollama
- ✅ Offline LLM execution
- ✅ Beginner-friendly AI workflow
- ✅ LangChain integration
- ✅ Python virtual environment setup
- ✅ AI-powered DevOps assistant
- ✅ Fully offline AI experimentation

---

# ⚙️ Installation Steps

## 1️⃣ Install Required Software

Install the following tools:

- Docker Desktop
- Python
- Git
- VS Code
- Ollama

---

## 2️⃣ Verify Installation

### Verify Docker

```bash
docker --version
```

### Verify Python

```bash
python --version
```

### Verify Git

```bash
git --version
```

### Verify Ollama

```bash
ollama --version
```
![alt](https://github.com/rohityt0dev/agentic-ai-devops/blob/a2ab47739e0b0be89eec2d900588fa6fcab1a792/day-01/SC/Screenshot%202026-05-16%20174339.png)
---

# 🚀 Run Your First Local LLM

## Start Ollama

```bash
ollama run phi3
```

## Test the Model

```bash
Explain Kubernetes like I am a beginner
```

---

# 📦 Create Your First AI DevOps Project

## Create Project Folder

```bash
mkdir ai-devops-lab
cd ai-devops-lab
```

---

## Create Python Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Required Python Packages

```bash
pip install openai langchain ollama rich
```

---

# 🧪 Build Your First AI Assistant

## Create `app.py`

```bash
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi3")

response = llm.invoke("Explain Git in simple words")

print("\nAI Response:\n")
print(response)
```

---

## Install LangChain Ollama Integration

```bash
pip install langchain-ollama
```

OR

```bash
python -m pip install langchain-ollama
```

---

## Run the Application

```bash
python app.py
```

---

# 🔄 AI Infrastructure Flow
![alt](https://github.com/rohityt0dev/agentic-ai-devops/blob/608cc5733d175957a052de0e54c484640bebf2f8/day-01/SC/ChatGPT%20Image%20May%2019%2C%202026%2C%2006_48_38%20PM.png)

---

# 📸 Screenshots

Add screenshots inside the `screenshots/` folder.

```bash
screenshots/
├── ollama-running.png
├── ai-response.png
└── project-setup.png
```

| Ollama Running | AI Response |
|----------------|-------------|
| Add Screenshot | Add Screenshot |

---

# 🎯 Learning Outcomes

By completing this project, you will understand:

- AI fundamentals
- Local LLM execution
- AI agent basics
- AI-powered DevOps workflows
- LangChain integration
- Offline AI infrastructure

---

# 👨‍💻 Author

## Tambadkar Rohit Yashwant

- DevOps & Cloud Enthusiast
- Learning AI Infrastructure Engineering
- Exploring LLMOps, Kubernetes, and AI Automation

---

# 📚 Next Step

➡️ Day 2: Understanding LLMs, Tokens, Embeddings, and Prompt Engineering
