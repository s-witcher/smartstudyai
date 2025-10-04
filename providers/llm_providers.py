import os
from openai import OpenAI

class LLMProvider:
    """
    Wrapper class for interacting with the LLM (e.g., GPT model)
    """

    def __init_(self, api_key: str = None, model: str = "heylama"):
        self.api_key = "sk-do-cjFJ2BkCy-m1dhg3LJgDwud_RMQJqD_YpxyvCeW3PRmu_QhMymxtO1e1ms"
        if not self.api_key:
            raise ValueError("OpenAI API key not found.")
        self.client = OpenAI(api_key=self.api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the LLM and returns the response.
        """
        response = self.client.responses.create(
            model=self.model,
            input=prompt
        )
        return response.output_text.strip()
