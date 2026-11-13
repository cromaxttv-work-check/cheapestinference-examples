#!/usr/bin/env python3
"""
Esempio CheapestInference con Anthropic SDK (Python)
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CHEAPESTINFERENCE_API_KEY")
if not api_key:
    raise ValueError("Imposta CHEAPESTINFERENCE_API_KEY nel file .env")

client = Anthropic(
    api_key=api_key,
    base_url="https://api.cheapestinference.com/anthropic",
)

def chat(prompt: str, model: str = "glm-5.3", max_tokens: int = 1024):
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return message.content[0].text

if __name__ == "__main__":
    print("=== CheapestInference - Anthropic SDK ===\n")

    risposta = chat("Scrivi un haiku sul codice.")
    print("Risposta:")
    print(risposta)
