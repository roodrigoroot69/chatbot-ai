import openai
from dataclasses import dataclass
from typing import Dict


@dataclass
class OpenAIWrapper:
    api_key: str
    organization_id: str

    def __post_init__(self):
        openai.api_key = self.api_key
        self.client = openai

    def send(self) -> Dict:
        return self.client.Completion.create(
            engine="gpt-3.5-turbo",
            prompt="¿Qué es ChatGPT?",
            max_tokens=20
            )
