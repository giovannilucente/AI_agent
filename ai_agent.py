import requests
import json
from abc import ABC, abstractmethod

class AIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 2048) -> str:
        pass

class OllamaProvider(AIProvider):
    def __init__(self, model: str, url: str):
        self.model = model
        self.url = url
    
    def generate(self, prompt: str, max_tokens: int = 2048) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {"num_predict": max_tokens}
        }
        try:
            response = requests.post(self.url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "[Nessuna risposta da Ollama]")
        except Exception as e:
            raise Exception(f"Error calling Ollama: {e}")

def create_ollama_ai_provider() -> AIProvider:
    """Factory to create the ollama AI provider."""
    
    model = "qwen2:7b-instruct"
    url = "http://localhost:11434/api/generate"
    return OllamaProvider(model, url)
