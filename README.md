# AI agent
This repository contains the script to run an AI agent that has the capability to have memory of past conversations.
In particular, the repository provides a Python interface to Ollama, an open-source local LLM server, allowing users to generate text with the ```Qwen2:7b-instruct``` model.

Open-source LLM server: Ollama runs locally on your machine and provides an HTTP API for inference.
The repository contains a Python script that connects to Ollama’s local API endpoint (http://localhost:11434/api/generate) to send prompts and receive generated responses. 
Requires 8GB+ RAM for good performance. The implementation of 

## Installation and Setup 
To install and run this project locally, follow these steps:
### Clone the repository
Clone the repository to your local machine:
```bash
git clone https://github.com/giovannilucente/AI_agent.git
cd AI_agent
```

### Install Ollama
Install Ollama:
```bash
curl -fsSL https://ollama.com/install.sh | sh
``` 

### Pull the LLM model
Download the model using this script:
```bash
ollama pull qwen2:7b-instruct
```
Check the downloaded model:
```bash
ollama list
```

### Start the Ollama server
The server must run to accept API requests. Start in a separate terminal:
```bash
ollama serve
```
This starts the server at ```http://localhost:11434```. Leave this terminal open while using the Python script.

Run this script to check the connection with the model:
```bash  
curl http://localhost:11434/api/tags
```
Run ```ps aux | grep ollama```  to check the processes and ``` sudo kill -9 <pid>``` to stop the server.
