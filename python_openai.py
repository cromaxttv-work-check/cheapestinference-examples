#!/usr/bin/env python3
"""
Esempio CheapestInference con OpenAI SDK (Python)
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("CHEAPESTINFERENCE_API_KEY")
if not api_key:
    raise ValueError("Imposta CHEAPESTINFERENCE_API_KEY nel file .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.cheapestinference.com/v1",
)

def chat(prompt: str, model: str = "glm-5.3"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Sei un assistente utile e conciso."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("=== CheapestInference - OpenAI SDK ===\n")

    # Lista modelli disponibili
    print("Modelli disponibili:")
    models = client.models.list()
    for m in models.data:
        print(f"  - {m.id}")
    print()

    # Chat semplice
    risposta = chat("Spiega in due frasi cos'è un LLM.")
    print("Risposta:")
    print(risposta)
