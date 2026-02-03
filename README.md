# AI_agent
This repository contains the script to run an AI agent that has the capability to have memory of past conversations.
In particular, the repository provides a Python interface to Ollama, an open-source local LLM server, allowing users to generate text with the ```Qwen2:7b-instruct``` model.

Open-source LLM server: Ollama runs locally on your machine and provides an HTTP API for inference.
Python integration: The repository contains a Python script that connects to Ollama’s local API endpoint (http://localhost:11434/api/generate) to send prompts and receive generated responses.


## Set up
Install OLLama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
``` 
