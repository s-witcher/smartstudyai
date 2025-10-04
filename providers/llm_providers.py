import os
import requests

class DOAIProvider:
    """
    LLM provider that uses DigitalOcean Inference API.
    """
    def __init__(self, api_key=None, model="openai-gpt-oss-120b"):
        self.api_key = "sk-do-tZCH12QV7kxevaLMGoOBNWxHvP7pdD4Ya_WrtyrqGRiyNsipSJDs9qQive"
        if not self.api_key:
            raise ValueError("Missing DigitalOcean API key.")
        self.model = model
        self.url = "https://inference.do-ai.run/v1/chat/completions"

    def generate(self, prompt: str) -> str:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(self.url, headers=headers, json=data)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
        else:
            raise RuntimeError(
                f"API Error {response.status_code}: {response.text}"
            )
